# simple guess the number game that allows the user 10 tries to guess the random number between 1- 100
import random


def guess_the_number():
    secret_number = random.randint(1, 100)
    attempts = 0
    max_attempts = 10

    print("Welcome to the Number Guessing game!")
    print("Please Guess a Number between 1 and 100")

    while attempts < max_attempts:
        guess = int(input("Take a guess\n"))
        attempts += 1

        if guess < secret_number:
            print(f"Too low! guess again:)\n")
        elif guess > secret_number:
            print(f"Too high! guess again:)\n")
        else:
            print(f"Congrats! You guessed the number!!!")
            break

        if attempts >= max_attempts:
            print("Sorry you have guessed too many times:( GAME OVER")


if __name__ == "__main__":
    guess_the_number()
