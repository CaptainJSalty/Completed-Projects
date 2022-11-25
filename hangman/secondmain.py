import os
import random

import hangman_words ################

import hangman_art
print(hangman_art.logo)
chosen_word = random.choice(hangman_words.word_list) ################

def choose_word ():
  chosen_word = random.choice(hangman_words.word_list) ################

display = []
for _ in range(len(chosen_word)):
  display += "_"
  

word_used = []


end_of_game = False
lives = 6

while end_of_game == False: 
  print(chosen_word)
  guess = input("Guess a letter: ").lower()
  word_used.append(guess)
 

  if guess in chosen_word: 
    
  #   #print(f"You have already used this {guess}")
   for position in range(len(chosen_word)):
      letter = chosen_word[position]
      #print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
      if letter == guess:
          display[position] = letter

  os.system('cls')
  if guess not in chosen_word: 

    lives -= 1 
    print(f"You guess {guess}, that's not in the word. You lose a life")
    os.system('cls')
    if lives == 0:
      print("Game Over")
      restart = input("Would you like to play again? Type 'yes' if you want to go again. Otherwise type 'no'.\n")
      if restart == "yes": 
        chosen_word = ''
        end_of_game = False 
        lives = 6
        # display.clear()
        # word_used.clear()
      else:
        end_of_game = True 
        print("You lose.")


  if "_" not in display: 
   
    print("You win!!!")
    choose_word()
    # print("Please press enter to continue or space to end") 
    restart = input("Would you like to play again? Press any button. Otherwise type 'no'.\n")
    if restart == "no":
        
        end_of_game = True 
        print("Game Over\nThank you for playing the game")
        print(hangman_art.ending)
    
    # restart == "yes": 
    #     os.system('cls')
    #     #chosen_word = ''
    #     lives = 6
    #     display.clear()
    #     word_used.clear()
    #     chosen_word = random.choice(hangman_words.word_list)
    #     for _ in range(len(chosen_word)):
    #       display += "_"
        
    #     end_of_game = False 
    else:
        os.system('cls')
        #chosen_word = ''
        lives = 6
        display.clear()
        word_used.clear()
        chosen_word = random.choice(hangman_words.word_list)
        for _ in range(len(chosen_word)):
          display += "_"
        
        end_of_game = False 
   

  if end_of_game == False: 
      
    from hangman_art import stages
    print(stages[lives])

    print(display)
    print ("letters used: ", word_used)
    print(f"You have {lives} lives left")




  
