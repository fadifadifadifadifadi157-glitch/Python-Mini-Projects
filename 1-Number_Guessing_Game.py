import random


def number_guessing_game():
    print("Welcome to the Number Guessing Game!")

    while True:
        print("\nI'm thinking of a number between 1 and 10...")

        secret_number = random.randint(1, 10)
        max_attempts = 3
        attempts = 0

        while attempts < max_attempts:
            try:
                remaining_attempts = max_attempts - attempts
                print(f"Attempts remaining: {remaining_attempts}")

                guess = int(input("Enter your guess: "))

                if guess < 1 or guess > 10:
                    print("Please enter a number between 1 and 10.")
                    continue

                if guess == secret_number:
                    print(
                        f"Congratulations! You guessed the number "
                        f"{secret_number} correctly!"
                    )
                    break

                elif guess < secret_number:
                    print("Too low! Try again.")

                else:
                    print("Too high! Try again.")

                attempts += 1

            except ValueError:
                print("Invalid input! Please enter a valid number.")

        if attempts == max_attempts and guess != secret_number:
            print(f"Game over! The correct number was {secret_number}.")

        play_again = input(
            "\nDo you want to play again? (yes/no): "
        ).lower()

        if play_again != "yes":
            print("Thanks for playing! Goodbye.")
            break


number_guessing_game()
