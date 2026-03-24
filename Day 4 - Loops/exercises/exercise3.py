# Exercise 3 — Sum of Numbers

# Ask user for a number n

# Compute:

# 1 + 2 + 3 + ... + n

user = int(input("Enter a number: "))

sum = 0

for i in range(1, user + 1):
    sum += i
print(sum)