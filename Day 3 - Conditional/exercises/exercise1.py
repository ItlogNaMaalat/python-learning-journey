# Exercise 1 — Even, Odd, or Zero

user = int(input("Enter a number: "))

if user == 0:
    print("Zero")
elif user % 2 == 1 :
    print("odd")
else:
    print("even")