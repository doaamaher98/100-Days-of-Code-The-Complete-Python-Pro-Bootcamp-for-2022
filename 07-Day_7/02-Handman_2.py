import random

word_list = ["ardvark", "baboon", "camel"]

chosen_word = random.choice(word_list)
# Generate another list of the chosen_word all of ["_","_",...]
display_list = []

# Enter the word's chars in display_list with "_" instead of chars
for letter in chosen_word:
    display_list.append("_")
    
guess = input("Guess a letter : ").lower()

length_of_word = len(chosen_word)
i = 0
# Loop through each position in chosen_word to match the guess letter
for letter in chosen_word:
    if letter == guess and i < length_of_word:
        display_list[i] = letter
    else:
        pass
    i+=1
    
print(display_list)