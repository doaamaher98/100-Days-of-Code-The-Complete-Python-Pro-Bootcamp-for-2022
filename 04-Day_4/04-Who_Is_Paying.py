'''
    Select a random name from a list of names, the person selected will have to pay for the rest. 
    split the names_string into individual names and put them inside a list called names. 
    split(" "), splits names after each space, it outputs a list
'''

import random 

names_string = input ("Give me everybody's names, seperated by a comma.\n")

names = names_string.split(", ")
count_names = len(names)

the_one_to_pay_int = random.randint(0, count_names-1)
random_person = names[the_one_to_pay_int]

# random_person = random.choice(names)

print(f"{random_person} will pay this bill ;)")

'''
Nested lists [lists inside lists] 
'''
fruits = ["Strawberries", "Apples", "Grapes"]
vegetables = ["Kale", "Tomatoes", "Potatoes"]

all_fruits_vegies = [fruits, vegetables]
print (all_fruits_vegies)