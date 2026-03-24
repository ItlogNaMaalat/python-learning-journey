# Exercise 5 - Pattern Printer
# input: n = 5

# Output:
# *
# **
# ***
# ****
# *****

# rows = 5

for i in range(1, 6):
    for j in range(i):
        print("*", end=" ")
    print()


