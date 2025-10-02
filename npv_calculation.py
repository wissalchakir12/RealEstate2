# npv_calculation.py

# Given data
initial_investment = 110000
cash_flows = [3200, 3200, 3200, 3200, 3200, 3200, 3200, 3200, 3200, 3200, 3200, 3200]
discount_rate = 0.08

# Calculate NPV manually
npv = -initial_investment
for t, cf in enumerate(cash_flows, 1):
    npv += cf / ((1 + discount_rate) ** t)

# Output the result
npv_result = npv