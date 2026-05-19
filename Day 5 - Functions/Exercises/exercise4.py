# Exercise 4 — Password Checker

## Task: def check_password(input_password):

# Return:
# True if correct
# False if wrong

input_password = str(input("Enter a Password: "))

def check_password(input_password):
    correct_password = "python123"

    if input_password == correct_password:
        return True
    else:
        return False
print(check_password(input_password))