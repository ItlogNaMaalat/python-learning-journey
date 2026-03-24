# Exercise 2 — Login System

# Ask:
#   username
#   password

# Correct values:
#   username = "admin"
#   password = "1234"

# Print:
#   "Login successful"
#   "Invalid credentials"

username = input("Username: ")
password = str(input("Password: "))

if username == 'admin' and password == '1234':
    print("login Succesfully!")
else:
    print("Invalid credentials") 
