# Exercise 1 — Count Even Numbers

# Ask user for a number n

# Print all EVEN numbers from 1 to n

user = int(input("Enter a number: "))

for i in range(1, user + 1):
   if i % 2 == 0:
      print(i)