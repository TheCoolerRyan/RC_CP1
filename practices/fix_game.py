#RC, 1st, Fix the Game

import random
def start_game():
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    number_to_guess = random.randint(1, 100)
    max_attempts = 10
    attempts = 0
    game_over = False
    while not game_over:
        if attempts >= max_attempts:     # We put this in the wrong spot, Logic, You had 11 attempts instead of ten and if you got it right on the 11 it would just say you ran out of guesses.
            print(f"Sorry, you've used all {max_attempts} attempts. The number was {number_to_guess}.")
            game_over = True
        guess = int(input("Enter your guess: "))  #It was a string instead of a integer, Syntax, made it so when it checked if it was greater then it would come up with an error and break everything.
        if guess == number_to_guess:    #The elif was an if instead of an elif, Syntax, You can't have to ifs right after each other.
            print("Congratulations! You've guessed the number!")
            game_over = True
        elif guess > number_to_guess:
            print("Too high! Try again.")
        elif guess < number_to_guess:
            print("Too low! Try again.")  
        attempts += 1     #The attempts never went up, Runtime, made it so you had ifinite attempts.
        continue
    print("Game Over. Thanks for playing!")
start_game()