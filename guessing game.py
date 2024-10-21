import random

def guessing_game():
    number_to_guess = random.randint(1, 50)
    guess = None

    print("I'm thinking of a number between 1 and 50. Can you guess what it is?")

    while guess != number_to_guess:
        guess = int(input("Enter your guess: "))
        
        if guess < number_to_guess:
            print("Aim a little higher next time!!")
        elif guess > number_to_guess:
            print("oof too high...try a little lower")
        else:
            print("Goog job! You guessed correctly :) ")

guessing_game()