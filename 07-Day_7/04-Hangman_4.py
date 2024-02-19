import random

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']


word_list = ["ardvark", "baboon", "camel"]

chosen_word = random.choice(word_list)
# Generate another list of the chosen_word all of ["_","_",...]
display_list = []

# Enter the word's chars in display_list with "_" instead of chars
for letter in chosen_word:
    display_list.append("_")

length_of_word = len(chosen_word)

i = 0
stage_num = 0

while stage_num != 6 :
    guess = input("Guess a letter : ").lower()
    i=0
    
    if guess not in chosen_word:
        stage_num +=1
        print(stages[stage_num])
    else :
        print(stages[stage_num])
        
    # Loop through each position in chosen_word to match the guess letter
    for letter in chosen_word:  
        if letter == guess and i < length_of_word:
            display_list[i] = letter
        
        else:
            pass
        i+=1
    
    print(display_list)
    
if (display_list == chosen_word):
        print("You Won!")
else :
    print(stages[6])
    print ("You Lose!")