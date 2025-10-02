# irr_calculation.py

def calculate_irr(cash_flows, max_iterations=1000, tolerance=1e-6):
    """Calculate Internal Rate of Return (IRR) using the Newton-Raphson method."""
    
    def npv(rate):
        return sum(cf / ((1 + rate) ** i) for i, cf in enumerate(cash_flows))
    
    def npv_derivative(rate):
        return sum(-i * cf / ((1 + rate) ** (i + 1)) for i, cf in enumerate(cash_flows))
    
    # Initial guess
    rate = 0.1
    
    for _ in range(max_iterations):
        npv_val = npv(rate)
        npv_deriv = npv_derivative(rate)
        new_rate = rate - npv_val / npv_deriv
        
        if abs(new_rate - rate) < tolerance:
            return new_rate
        
        rate = new_rate
    
    return rate

# Given data
cash_flows = [-110000, 3200, 3200, 3200, 3200, 3200, 3200, 3200, 3200, 3200, 3200, 3200, 3200]

# Calculate IRR
irr = calculate_irr(cash_flows) * 100  # Convert to percentage

# Output the result
irr_result = irr