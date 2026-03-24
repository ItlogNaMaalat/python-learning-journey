# Exercise 1 — Even, Odd, or Zero

# Ask user for a number

# Print:
#   "Zero" if 0
#   "Even" if divisible by 2
#   "Odd" otherwise

user = int(input("Enter a number: "))

if user == 0:
    print("Zero")
elif user % 2 == 1 :
    print("odd")
else:
    print("even")