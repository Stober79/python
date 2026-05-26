capital = 5000
interest_rate = 0.08
inflation_rate = 0.15

# Calculate the real interest rate
real_interest_rate = interest_rate - inflation_rate 
print(real_interest_rate) 
capital = capital * (1 + interest_rate)
print(capital)
capital_afterInflation = capital * (1 - inflation_rate)
print(capital_afterInflation)  