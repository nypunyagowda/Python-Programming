import random

# Computer chooses a random number between 1 and 100
secret_number = random.randint(1, 100)

print("🎮 Welcome to the Number Guessing Game!")
print("I have chosen a number between 1 and 100.")
print("Try to guess it!")

attempts = 0

while True:
    guess = int(input("Enter your guess: "))
    attempts += 1

    if guess < secret_number:
        print("Too low! Try again.")
    elif guess > secret_number:
        print("Too high! Try again.")
    else:
        print("🎉 Congratulations!")
        print("You guessed the number correctly.")
        print("Number of attempts:", attempts)
        break
