# npv_irr_calculator.py
import numpy_financial as npf

# Cash flow data
initial_investment = -2250000  # Down payment
monthly_rental_income = 75000
monthly_expenses = 12000
monthly_loan_payment = 35230.34
analysis_period_years = 10

# Calculate monthly net cash flow
monthly_net_cash_flow = monthly_rental_income - monthly_expenses - monthly_loan_payment

# Create an array of cash flows (monthly)
cash_flows = [monthly_net_cash_flow] * (analysis_period_years * 12)

# Add the initial investment at the beginning (time 0)
cash_flows.insert(0, initial_investment)

# Calculate NPV
discount_rate_annual = 0.1  # 10% annual discount rate
discount_rate_monthly = (1 + discount_rate_annual) ** (1/12) - 1
npv = npf.npv(discount_rate_monthly, cash_flows)

# Calculate IRR
irr = npf.irr(cash_flows) * 12  # Convert monthly IRR to annual IRR

result = {"npv": npv, "irr": irr}