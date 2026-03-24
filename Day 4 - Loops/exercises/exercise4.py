# Exercise 4 — Number Guessing Game

# Set secret number = 7
# User keeps guessing until correct

# Print:
#   “Too high”
#   “Too low”
#   “Correct!”

guess = int(input("Guess a number: "))

secret = 7

while guess != secret:
    if guess > secret:
        print("Too high")
        guess = int(input("Guess a number: "))

    elif guess < secret:
        print("Too low")
        guess = int(input("Guess a number: "))
    
print("Correct!")
    