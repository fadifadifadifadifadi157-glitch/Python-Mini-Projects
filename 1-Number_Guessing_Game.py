import random

def number_guessing_game():
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 10...")

    # Generate a random number between 1 and 10
    secret_number = random.randint(1, 10)

    # Maximum number of attempts
    max_attempts = 3
    attempts = 0

    # Start the game loop
    while attempts < max_attempts:
        try: # Remaining Attempts
            remaining_attempts = max_attempts - attempts
            print(f"Attempts remaining: {remaining_attempts}")
            # Get user's guess
            guess = int(input("Enter your guess: "))
            if guess < 1 or guess > 10:
              print("Please enter a number between 1 and 10.")
              continue

            # Check if the guess is correct
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

            # Increase the number of attempts
            attempts += 1

        except ValueError:
            print("Invalid input! Please enter a valid number.")

    # If max attempts reached and no correct guess
    if attempts == max_attempts and guess != secret_number:
        print(f"Game over! The correct number was {secret_number}.")

    # Ask to play again
    play_again = input(
        "\nDo you want to play again? (yes/no): "
    ).lower()

    if play_again == "yes":
        number_guessing_game()
    else:
        print("Thanks for playing! Goodbye.")


# Run the game
number_guessing_game()
