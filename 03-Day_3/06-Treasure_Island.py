print ('''
       *******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/________
*******************************************************************************
''')


print("Welcome to Tresure Island.")
print("Your mission is to find the treasure.")

direction_in_cross_road = input('You\'re at a cross road. Where do you want to go? Type "left" or "right"\n').lower()

if direction_in_cross_road == 'left':
    lake_action = input('You come to a lake. There is an island in the middle of the lake. Type "wait" to wait for a boat. Type "swim" to swim across\n').lower()
    
    if lake_action == 'wait' :
        island_doors = input("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue, which one do you choose?\n").lower()
        if island_doors == 'red':
             print("You enter a room of beasts.")
             
        elif island_doors == 'yellow' :
            print("YOU WIN!")
            
        elif island_doors == 'blue':
            print("You enter a room of beasts. Game Over.")
            
        else:
          pass
        
    elif lake_action == 'swim' :
        print("Game Over.")
    else:
      pass
  
elif direction_in_cross_road == 'right':
    print("Game Over.")