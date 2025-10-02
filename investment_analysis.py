# Investment Analysis for Casablanca Property

import numpy as np

# Property details
property_value = 4500000  # MAD
monthly_rent = 35000     # MAD
down_payment_percent = 0.20
loan_term = 20          # years
interest_rate = 0.05    # annual

# Financing details
down_payment = property_value * down_payment_percent
loan_amount = property_value - down_payment

# Annual cash flow (after all expenses)
annual_rent = monthly_rent * 12
property_tax_rate = 0.01  # 1% of property value annually
maintenance_cost = property_value * 0.01  # 1% of property value annually
insurance_cost = 3000     # MAD per year
management_fee = annual_rent * 0.05  # 5% of rental income
vacancy_rate = 0.05      # 5% vacancy rate

annual_expenses = (
    property_value * property_tax_rate +
    maintenance_cost +
    insurance_cost +
    management_fee +
    annual_rent * vacancy_rate
)

# Monthly mortgage payment calculation
monthly_interest_rate = interest_rate / 12
num_payments = loan_term * 12

# Handle the case where monthly_interest_rate is 0 to avoid division by zero
if abs(monthly_interest_rate) < 1e-10:
    monthly_mortgage = loan_amount / num_payments
else:
    monthly_mortgage = (loan_amount * monthly_interest_rate * (1 + monthly_interest_rate)**num_payments) / ((1 + monthly_interest_rate)**num_payments - 1)

annual_mortgage = monthly_mortgage * 12

# Annual cash flow
annual_cash_flow = annual_rent - annual_expenses - annual_mortgage

# Investment analysis for different periods
def calculate_metrics(period):
    # Cash flows array (simplified - assuming constant cash flow)
    cash_flows = [-(down_payment)] + [annual_cash_flow] * period
    
    # Calculate NPV at different discount rates
    def npv(rate, cash_flows):
        total = -cash_flows[0]  # Initial investment
        for i in range(1, len(cash_flows)):
            total += cash_flows[i] / (1 + rate)**i
        return total
    
    npv_5 = npv(0.05, cash_flows)
    npv_8 = npv(0.08, cash_flows)
    npv_10 = npv(0.10, cash_flows)
    
    # Calculate IRR using Newton-Raphson method
    def irr(cash_flows, max_iterations=1000, precision=1e-07):
        def npv_irr(rate):
            total = -cash_flows[0]
            for i in range(1, len(cash_flows)):
                total += cash_flows[i] / (1 + rate)**i
            return total
        
        guess = 0.1  # Initial guess of 10%
        for _ in range(max_iterations):
            npv_guess = npv_irr(guess)
            derivative = (npv_irr(guess + precision) - npv_guess) / precision
            if abs(derivative) < precision:
                break  # Avoid division by zero
            new_guess = guess - npv_guess / derivative
            if abs(new_guess - guess) < precision:
                return new_guess
            guess = new_guess
        return guess
    
    irr_value = irr(cash_flows)
    
    # Calculate ROI
    total_cash_in = down_payment
    total_cash_out = sum([cf for cf in cash_flows[1:] if cf > 0])
    roi = ((total_cash_out - total_cash_in) / total_cash_in) * 100
    
    # Calculate cumulative cash flow
    cumulative_cash_flow = np.cumsum(cash_flows)
    
    # Calculate payback period
    payback_period = None
    for i, cash_flow in enumerate(cumulative_cash_flow):
        if cash_flow > 0:
            payback_period = i
            break
    
    return {
        'npv': {'5%': npv_5, '8%': npv_8, '10%': npv_10},
        'irr': irr_value * 100,  # Convert to percentage
        'roi': roi,
        'cumulative_cash_flow': cumulative_cash_flow.tolist(),
        'payback_period': payback_period
    }

# Calculate for 5, 10, and 20 years
results = {
    '5_years': calculate_metrics(5),
    '10_years': calculate_metrics(10),
    '20_years': calculate_metrics(20),
    'annual_cash_flow': annual_cash_flow,
    'monthly_mortgage': monthly_mortgage,
    'annual_mortgage': annual_mortgage,
    'annual_expenses': annual_expenses,
    'annual_rent': annual_rent,
    'down_payment': down_payment,
    'loan_amount': loan_amount
}

# Additional calculations
cap_rate = (annual_rent - annual_expenses) / property_value
gross_rent_multiplier = property_value / annual_rent
debt_service_coverage_ratio = annual_rent / annual_mortgage

results['cap_rate'] = cap_rate
results['gross_rent_multiplier'] = gross_rent_multiplier
results['debt_service_coverage_ratio'] = debt_service_coverage_ratio

results