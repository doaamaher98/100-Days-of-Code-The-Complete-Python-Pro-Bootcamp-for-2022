import random 

option = input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for scissors\n")

# List
computer_options_list = [
    """
        _______
    ---'   ____)
        (_____)
        (_____)
        (____)
    ---.__(___)
    """, 
    """
        _______
    ---'    ____)____
            ______)
            _______)
            _______)
    ---.__________)
    """,
    """
        _______
    ---'   ____)____
            ______)
        __________)
        (____)
    ---.__(___)
    """
]

computer_option_int = 0

if option == '0':
    # Rock
    print("""
        _______
    ---'   ____)
        (_____)
        (_____)
        (____)
    ---.__(___)
    """)
    
    # Computer Option
    computer_option_int = random.randint(0, 2)
    print (f"Computer chooses :\n{computer_options_list[computer_option_int]}")
    
    if computer_option_int == 1 :
        print("You Win")
        
    elif computer_option_int == 2 :
        print("You lose")
        
    else:
      print("Draw")
   
elif option == '1':
    # Paper
    print("""
        _______
    ---'    ____)____
            ______)
            _______)
            _______)
    ---.__________)
    """)
    
    # Computer Option
    computer_option_int = random.randint(0, 2)
    print (f"Computer chooses :\n{computer_options_list[computer_option_int]}")
    
    if computer_option_int == 0 :
        print("You Win")
        
    elif computer_option_int == 2 :
        print("You Lose")
        
    else:
      print("Draw")
    
elif option == '2':
  # Scissors
    print("""
        _______
    ---'   ____)____
            ______)
        __________)
        (____)
    ---.__(___)
    """)
    
    # Computer Option
    computer_option_int = random.randint(0, 2)
    print (f"Computer chooses :\n{computer_options_list[computer_option_int]}")
    
    if computer_option_int == 0 :
        print("You Lose")
        
    elif computer_option_int == 1 :
        print("You Win")
        
    else:
      print("Draw")
      
else:
  print("Invalid number, you lose")