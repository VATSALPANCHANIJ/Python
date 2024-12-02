import random


def guess_number_game():
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")

    # The computer picks a random number
    secret_number = random.randint(1, 100)
    attempts = 0
    guessed = False

    while not guessed:
        try:
            # User input
            user_guess = int(input("Make a guess: "))
            attempts += 1

            if user_guess < secret_number:
                print("Too low! Try again.")
            elif user_guess > secret_number:
                print("Too high! Try again.")
            else:
                print(f"Congratulations! You've guessed the number {secret_number} in {attempts} attempts.")
                guessed = True
        except ValueError:
            print("Please enter a valid number.")


# Start the game
guess_number_game()
