monthly_salary = int(input("Enter your monthly income: "))
total_expenses = int(input("Enter your total monthly expenses: "))
savings = monthly_salary - total_expenses
annual_interest_rate = 0.05
projected_savings = savings * 12 + (savings * 12 * annual_interest_rate)
print(f"Your monthly savings are ${savings}.")
print(f"Projected savings after one year, with interest, is: ${int (projected_savings)}.")