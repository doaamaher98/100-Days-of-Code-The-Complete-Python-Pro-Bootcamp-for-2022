import random
import os

import Hangman_Art
import Hangman_Names

clear = lambda: os.system('cls')

chosen_word = random.choice(Hangman_Names.word_list)
# Generate another list of the chosen_word all of ["_","_",...]
display_list = []

# Enter the word's chars in display_list with "_" instead of chars
for letter in chosen_word:
    display_list.append("_")

length_of_word = len(chosen_word)

i = 0
stage_num = 0

print (Hangman_Art.logo)


while stage_num != 6 :
    
    guess = input("Guess a letter : ").lower()
    clear()
    i=0
    
    if guess not in chosen_word:
        stage_num +=1
        print(Hangman_Art.stages[stage_num])
    else :
        print(Hangman_Art.stages[stage_num])
        
    # Loop through each position in chosen_word to match the guess letter
    for letter in chosen_word:  
        if letter == guess and i < length_of_word:
            display_list[i] = letter
        
        else:
            pass
        i+=1
    
    print(display_list)
    
if (display_list == chosen_word):
    clear()
    print("You Won!")
else :
    clear()
    print(Hangman_Art.stages[6])
    print ("You Lose!")