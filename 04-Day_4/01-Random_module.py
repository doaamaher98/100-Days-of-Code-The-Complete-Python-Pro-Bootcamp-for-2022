import random

# importing my module
import my_module 

random_integer = random.randint(100, 200)

# Generates a random integer between 100 and 200 including them
print(random_integer)

# Print the pi value from the other module
# module.value 

print (my_module.pi)

# Generate a random floating point number
# 1. between 0 and 1 (where 1 isnt included)
random_floating = random.random()
print(random_floating)

# 2. any range [1->5], 5 isnt included
random_float_bigger = (random.random() * 5)
print(random_float_bigger)