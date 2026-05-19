# Exercise 5 (CHALLENGE 🔥🔥)

# Number Analyzer Function
# Create:
# def analyze_number(num):

# Return:
# "Positive Even"
# "Negative Odd"
# "Zero"

num = int(input("Enter a number: "))

def analyze_number(num):
    if num > 1 and num % 2 == 0:
        return "Positive and even number"
    elif num <= -1 and num % 2 == 0:
        return "Negative and even number"
    elif num > 1 and num % 2 == 1:
        return "Positive and odd number"
    elif num <= -1 and num % 2 == 1:
        return "Negative and odd number"
    else:
        return "Zero"
print (analyze_number(num))