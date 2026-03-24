# Exercise 4 (Number Classification System)

# Ask user for a number:

# Check:
#   positive / negative / zero
#   even or odd

# Output example:
#   Positive and Even
#   Negative and Odd
#   Zero

user = int(input("Enter a number: "))

if user >= 1 and user % 2 == 1:
    print("Positive and odd")
elif user >= 1 and user % 2 == 0:
    print("Positive and even")
elif user < -1 and user % 2 == 1:
    print("negative and odd")
elif user < -1 and user % 2 == 0:
    print("negative and even")
else:
    print("Zero")