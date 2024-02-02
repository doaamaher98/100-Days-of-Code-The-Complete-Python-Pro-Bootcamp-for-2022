import random 

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '@', '$', '%', '^', '&', '*', '(', ')', '_', '+']

print("Welcome to the PyPassword Generator!")

letters_num = int(input("How many letter would you like in your password\n"))
symbols_num = int(input("How many symbols would you like in your password\n"))
numbers_num = int(input("How many numbers would you like in your password\n"))

random_letter = 0
random_num    = 0
random_symbol = 0

generated_password = ""

''' Easy Way '''
# for l in range(0, letters_num):
#     random_letter = random.randint(0,len(letters))
#     l = letters[random_letter]
#     generated_password += l
#     # Or use random.choice(letters)

# for s in range(0, symbols_num):
#     random_symbol = random.randint(0, len(symbols))
#     s = symbols[random_symbol]
#     generated_password += s
#     # Or use random.choice(symbols)
 
# for n in range(0, numbers_num):
#     random_num = random.randint(0, len(numbers))
#     generated_password += str(random_num)
#     # Or use random.choice(numbers)
       
# print("-------------------------------------------------")                   
# print(f"Password is : {generated_password}")

''' Hard Way '''
generated_password_list = []

final_password = ""

for l in range(0, letters_num):
    random_letter = random.randint(0,len(letters))
    l = letters[random_letter]
    generated_password_list += l
    # Or use random.choice(letters)

for s in range(0, symbols_num):
    random_symbol = random.randint(0, len(symbols))
    s = symbols[random_symbol]
    generated_password_list += s
    # Or use random.choice(symbols)
 
for n in range(0, numbers_num):
    random_num = random.randint(0, len(numbers))
    generated_password_list += str(random_num)
    # Or use random.choice(numbers)
    
# Shuffle the list
random.shuffle(generated_password_list)

# print(f"Password is : {generated_password_list}")

# Turn the list to a string
for char in generated_password_list :
    final_password += char
    
print(final_password)