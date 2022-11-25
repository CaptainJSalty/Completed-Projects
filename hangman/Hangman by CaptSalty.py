import os
import random
import time
import hangman_words ################

import hangman_art
print(hangman_art.logo)

chosen_word = random.choice (hangman_words.word_list)
display = [] 
for _ in range(len(chosen_word)):
    display += "_"


word_used = []
lives = 6
end_of_game = False

while end_of_game == False: 
    
    guess = input("Guess a letter: ").lower() 
    word_used.append(guess)


    if guess in chosen_word:

        for position in range(len(chosen_word)): 
            letter = chosen_word[position]
            if letter == guess: 
                display[position] = letter

        os.system('cls')

    if guess not in chosen_word: 

        lives -= 1 
        os.system('cls')
        print(f"You guessed {guess}, that's not in the word. You lose a life :/")
        
        if lives == 0: 
            os.system('cls')
            print(hangman_art.game_over)
            restart = input("Would you like to play again? Press enter to play again or type 'no.' ")

            if restart == "no":

                os.system('cls')

                print(f"Thank you for playing the game!\nThe program will close in 5 seconds")
                print(hangman_art.ending)
                time.sleep(4)

                end_of_game = True 
            else:
                os.system('cls')
                lives = 6
                display.clear()
                word_used.clear()
                chosen_word = random.choice(hangman_words.word_list)
                for _ in range(len(chosen_word)):
                 display += "_"




    if "_" not in display:

        print(hangman_art.win)
        #choose_word()

        restart = input("Would you like to play again? Press enter to play again or type 'no.' ")

        if restart == "no":

            os.system('cls')

            print(f"Thank you for playing the game!\nThe program will close in 5 seconds")
            print(hangman_art.ending)
            time.sleep(4)

            end_of_game = True 
        else:
            os.system('cls')
            lives = 6
            display.clear()
            word_used.clear()
            chosen_word = random.choice(hangman_words.word_list)
            for _ in range(len(chosen_word)):
                display += "_"


    from hangman_art import stages
    print(stages[lives])

    print(display)
    print ("letters used: ", word_used)
    print(f"You have {lives} lives left")
