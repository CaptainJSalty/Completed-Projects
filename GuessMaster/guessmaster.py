from random import randint
import os
from art import logo



EASY_LEVEL = 10 
HARD_LEVEL = 5



def difficulty ():
    level = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if level == "easy": 
        return EASY_LEVEL
    else:
        return HARD_LEVEL




def check_answer(guess, answer, turns):

    if guess > answer: 
        print("Too High.")
        return turns - 1
    elif guess < answer: 
        print("Too Low.")
        return turns - 1 
    else:
        print(f"You got it! The answer was {answer}. ")


def game():
    print(logo)
    print("Welcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 50.")
    answer = randint(1, 50)

    turns = difficulty ()

    guess = 0 
    while guess != answer: 
        print(f"You have {turns} attempts remaining to guess the number.")

        guess = int(input("Make a guess: "))

        #Track the number of turns and reduce by 1 if they get it wrong 

        turns = check_answer(guess, answer, turns)
        if turns == 0:
            print("You've run out of guesses, you lose.")
            return 

        elif guess != answer: 
            print("Guess again.")

  
game()