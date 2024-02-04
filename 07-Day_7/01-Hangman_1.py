import random


word_list = ["ardvark", "baboon", "camel"]

# Randomly choose a word of the above list
# chosen_word = random.randint(0,len(word_list)-1)
# # OR chosen_word = random.choice(word_list)

# # chosen_word = str(chosen_word)
# print(word_list[chosen_word])

# # Ask the user to guess a letter of the chosen word, make it = guess and lowercase
# guess = input("Guess a letter\n").lower()


# # Check if the guessed letter is at the chosen_word or not
# i = 0

# for i in word_list[i]:
#     if i == guess:
#         print("Right")
#     else :
#         print("Wrong")
        


# Another Solution        
chosen_word = random.choice(word_list)

guess = input("Guess a letter : ").lower()

for letter in chosen_word:
    if letter == guess:
        print("Right")
    else:
        print("Wrong")
