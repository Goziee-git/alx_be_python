monthly_income = int(input("Enter your monthly income: "))
monthly_expenses = int(input("Enter your monthly expenses: "))
monthly_savings = monthly_expenses - monthly_income
simple_interest_rate = 0.05
projected_savings = (monthly_savings * 12 + (monthly_savings * 12 * simple_interest_rate))
print("Your monthly savings are $",monthly_savings)
print("Projected savings after one year, with interest is: $",projected_savings)
