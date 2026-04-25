# Exercise 1 - Even or Odd Checker (using %)

# Ask user for a number
# Print:
#   “Even” if divisible by 2
#   “Odd” otherwise

number = float(input("Give me a number: "))

check = number % 2 


if check == 0:
    print("even")
else:
    print("odd")