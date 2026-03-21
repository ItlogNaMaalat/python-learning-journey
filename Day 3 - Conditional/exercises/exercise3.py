# Exercise 3 — Salary Bonus System

salary = int(input("your salary: "))
years_of_service = int(input("Years of Service: "))


if years_of_service >= 5:
    print(f"final salary: {(salary * .20) + salary}")
elif years_of_service >= 2:
    print(f"Final salary: {(salary * .10) + salary}")
else:
    print(f"Final salary: {(salary * .05) + salary}")