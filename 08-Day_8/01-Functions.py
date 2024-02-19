
# Creating Greet function
def greet():
    print("Hello")
    print("Welcome to Day 8 in the python course!")
    print("Hope you are ready!")
    

# Calling the function
greet()

print("***********************************************")


# Function with 1 parameters
def greet_with_name(name):
    print(f"Hello {name}")
    print("Welcome to Day 8 in the python course!")
    print("Hope you are ready!")
    
my_name = "Doaa"
greet_with_name(my_name)

print("***********************************************")

# Function with 2 parameters
def greet_with_name_and_address (name, address):
    print(f"Hello {name}")
    print(f"Your address is {address}, right?")
    
my_address = "Masr el Gedida"

greet_with_name_and_address(my_name,my_address)

# Calling with keywords arguments
greet_with_name_and_address(address="MASR EL GEDIDA", name="DOAA")
