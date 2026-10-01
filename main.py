import random
import msvcrt
import sys


def get_guess():
    while True:
        print("Enter your guess (1-100), or press ESC to exit: ", end="", flush=True)
        user_input = ""

        while True:
            key = msvcrt.getwch()

            if key == "\x1b":
                print("\nThanks for playing!")
                sys.exit()

            if key == "\r":
                print()
                break

            if key == "\b":
                if user_input:
                    user_input = user_input[:-1]
                    print("\b \b", end="", flush=True)
                continue

            if key.isdigit():
                user_input += key
                print(key, end="", flush=True)

        try:
            guess = int(user_input)

            if 1 <= guess <= 100:
                return guess

            print("Please enter a number between 1 and 100.")

        except ValueError:
            print("Please enter a valid number.")


def choose_difficulty():
    while True:
        print("\nChoose your difficulty:")
        print("1. Easy   - 15 attempts")
        print("2. Medium - 10 attempts")
        print("3. Hard   - 5 attempts")

        choice = input("Enter 1, 2, or 3: ").strip()

        if choice == "1":
            return 15
        elif choice == "2":
            return 10
        elif choice == "3":
            return 5
        else:
            print("Invalid choice. Please select 1, 2, or 3.")


def play_game():
    attempts = choose_difficulty()
    secret_number = random.randint(1, 100)

    print("\nI picked a number between 1 and 100.")
    print(f"You have {attempts} attempts to guess it.")

    while attempts > 0:
        print(f"\nAttempts remaining: {attempts}")
        guess = get_guess()
        attempts -= 1

        if guess == secret_number:
            print("You guessed the number! You win!")
            return

        if guess < secret_number:
            print("Too low!")
        else:
            print("Too high!")

    print(f"\nYou are out of attempts. The number was {secret_number}.")


def main():
    print("Welcome to the Dice Game!")
    input("Press ENTER to start...")

    while True:
        play_game()

        while True:
            play_again = input("\nWould you like to play again? (y/n): ").strip().lower()

            if play_again in ("y", "n"):
                break

            print("Please enter y or n.")

        if play_again == "n":
            print("Thanks for playing!")
            break


if __name__ == "__main__":
    main()
