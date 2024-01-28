# Primitive Data Types

# 1- Strings
print ("Hello"[0])  # prints H
# This is called subscripting.

# 2- Integers
print (1+2)         # prints 3

# 3- Float
print (1324.32)     

# 4- Boolean
## True or False

##########################################
# Type conversion (Casting)
num_char = len(input ("Enter your name : ")) # an integer

# Type before
print (type(num_char))

#print("Name has " + num_char + "characters") # cant happen as we cant concatenate integers to strings, so a type casting is required
casted_num_char = str(num_char)
print("Name has " + casted_num_char + " characters")

# Type after
print (type(casted_num_char))

##########################################
# Adding a 2-digit number code
num = input ("Enter a random 2-digit number :\n")

# Converting the int to str to be able to subscript
num_str = str(num)

# Sum them
sum = int(num_str[0] + num_str[1])

# Print result
print(sum)
##########################################
# Math Operations in Python :-

## Addition                         3+5
## Subtraction                      5-3
## Multiplication                   3*3
## Divison (always float result)    6/2
## Exponent                         2**3

# Priorities Rule :
    ## PEMDAS
        # 1) ()
        # 2) **
        # 3) *, / [LEFT TO RIGHT]
        # 4) +, - [LEFT TO RIGHT] 
        
print (((3 * (3 + 3)) / 3) - 3) # To get 3
