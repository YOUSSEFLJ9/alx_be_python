monthly_salary = float(input("Enter your monthly income: "))
total_expenses = float(input("Enter your total monthly expenses: "))
savings = monthly_salary - total_expenses
annual_interest_rate = 0.05
projected_savings = savings * 12 + (savings * 12 * annual_interest_rate)
print(f"Your monthly savings are ${int(savings)}.")
print(f"Projected savings after one year, with interest, is: ${int (projected_savings)}.")