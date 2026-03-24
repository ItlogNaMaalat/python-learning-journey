# Exercise 2 — Password Retry System

# Correct password:

# password = "python123"

# Ask user repeatedly until correct

password = str(input("Enter Password: "))

correct_pass = "python123"

while password != correct_pass:
    password = str(input("Enter Password: "))
    continue
