#Exercise 2 — Salary Breakdown

base_salary = float(input("Enter your Base Salary: "))
bonus = float(input("Enter your bonus: "))
tax_rate = float(input("Enter your tax rate: "))

gross = base_salary + bonus
tax = gross *(tax_rate/100)
net = gross - tax

print("your gross is ", gross)
print("your income tax is ", tax)
print("your net income is ", net)