# this is a command-line project that generates different randomly created passwords when run. This is very useful for one-time password uses or for keys where you want to store unique strings

import string, random
from time import sleep


def generate_password(length=5, numbers=True, special_characters=True):
    letters = string.ascii_letters
    digits = string.digits
    characters = string.punctuation
    combination = letters
    password = ""

    if numbers:
        combination += digits
    if special_characters:
        combination += characters

    for _ in list(combination):
        while len(password) < length:
            password += random.choice(combination)

    print(f"Your randomly generated password is:  {password}\nPlease keep it safe!")
    print("\nThank you for using my program!\n")


def main():
    print("\nThis is the Random Password Generator")

    min_length = int(
        input(
            "Please let us know the length of the password\n(Password must have a minimum length of 5): "
        )
    )

    if min_length < 5:
        print(
            "Oops, your choice is smaller than 5 \nOur program will automatically assume 5 as the number :)"
        )
        min_length = 5

    while True:
        numbers = input(
            "Would you like numbers in the password (Put Yes or No): "
        ).lower()

        match numbers:
            case "yes":
                numbers = True
                break
            case "no":
                numbers = False
                break
            case _:
                print("\nNot a valid choice, Please try again!!!")

    while True:
        special_chars = input(
            "Would you like special characters in the password (Put Yes or No): "
        ).lower()

        match special_chars:
            case "yes":
                special_chars = True
                break
            case "no":
                special_chars = False
                break
            case _:
                print("\nNot a valid choice, Please try again!!!")

    print(
        "\nWe are ready to prepare your password! \n\nPlease give us a few seconds..."
    )
    sleep(2)
    generate_password(min_length, numbers, special_chars)


if __name__ == "__main__":
    main()
