   ########### NUMBER GUESSER GAMING ###########

import random
def no_guessing_game():
    print("Welcome to the Number Guessing Game!")

    # Set the range for the random number
    lower_limit = 1
    upper_limit = 200
    secret_no = random.randint(lower_limit, upper_limit)
    
    attempts = 0

    while True:
        guess = int(input(f"Guess the number between {lower_limit} and {upper_limit}: "))
        if(guess>200):
            print("no. is in invalid RANGE ")
            break
        attempts += 1

        if guess == secret_no:
            print(f"Congratulations! You guessed the correct number {secret_no} in {attempts} attempts.")
            break
        elif guess < secret_no:
            print("Too low !!  please Try again.")
        else:
            print("Too high !! please Try again.")
no_guessing_game()