monthly_income = int(input("Enter your monthly income: "))
monthly_expenses = int(input("Enter your total monthly expenses: "))
>>>>>>> a5b8b8f41060beee932bcbab21746fbe0f43d815
monthly_savings = monthly_income - monthly_expenses
simple_interest_rate = 0.05
projected_savings = (monthly_savings * 12 + (monthly_savings * 12 * 0.05))
print("Your monthly savings are $",monthly_savings)
print("Projected savings after one year, with interest is: $",projected_savings)