import random
def guess_number_game():
    # Generate a random number between 1 and 100
    random_number = random.randint(1, 100)
    max_attempts = 10
    attempts = 0

    print("Welcome to the Guess A Number game!")
    print(f"Try to guess the number between 1 and 100. You have {max_attempts} attempts.")

    while attempts < max_attempts:
        try:

            guess = int(input("Enter your guess: "))


            if guess < 1 or guess > 100:
                print("Please enter a number between 1 and 100.")
                continue

            attempts += 1
# Check if the guess is too high, too low, or correct
            if guess < random_number:
                print("Too low!")
            elif guess > random_number:
                print("Too high!")
            else:
                print(f"Congratulations! You've guessed the number correctly in {attempts} attempts!")
                break
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    if attempts == max_attempts:
        print(f"Sorry! You've used all {max_attempts} attempts. The correct number was {random_number}.")


guess_number_game()
