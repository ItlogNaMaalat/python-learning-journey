# Exercise 1 - Created a personal profile program using variables and input.

# Ask the user for:
    # full name
    # age
    # height
    # favorite number

# Then print:
"""""
Hello [name]!
You are [age] years old and [height] meters tall.
Your favorite number is [number].
"""""

full_name = input("Enter your full name: ")
age = input("Enter your Age: ")
height = input("Enter your height(meters): ")
fav_num = input("What's your favorite number: ")

print(f"Hello,{full_name}!")
print(f"you are {age} years old and {height} meters tall.")
print(f"your favorite number is {fav_num}")
