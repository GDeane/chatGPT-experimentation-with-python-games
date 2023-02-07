import random

print("Welcome to the guessing game!")
number = random.randint(1, 100)
guess = int(input("Guess a number between 1 and 100: "))
tries = 1

while guess != number:
    if guess > number:
        print("Too high! Try again.")
    else:
        print("Too low! Try again.")
    guess = int(input("Guess a number between 1 and 100: "))
    tries += 1

print("Congratulations! You guessed the number in", tries, "tries.")