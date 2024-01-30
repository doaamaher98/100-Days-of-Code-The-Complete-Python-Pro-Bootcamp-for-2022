print ("Welcome to Python Pizza Deliveries!")

size = input("What Pizza size do you want? S, M or L :\n")
add_pepperoni = input("Do you want Pepperoni? Y or N :\n")
add_cheese = input ("Do you want extra cheese? Y or N :\n")

# Prices
small_pizza_cost = 15
medium_pizza_cost = 20
large_pizza_cost = 25

extra_pepperoni_small_pizza = 2
extra_pepperoni_medium_large_pizza = 3

extra_cheese = 1

final_cost = 0

if size == 'S' :
    final_cost = small_pizza_cost
    if add_pepperoni == 'Y' :
        final_cost += extra_pepperoni_small_pizza
    if add_cheese == 'Y' :
        final_cost += extra_cheese
    print (f"Your final bill is {final_cost}")
        
elif size == 'M' :
    final_cost = medium_pizza_cost
    if add_pepperoni == 'Y' :
        final_cost += extra_pepperoni_medium_large_pizza
    if add_cheese == 'Y' :
        final_cost += extra_cheese
    print (f"Your final bill is {final_cost}")
    
elif size == 'L' :
    final_cost = large_pizza_cost
    if add_pepperoni == 'Y' :
        final_cost += extra_pepperoni_medium_large_pizza
    if add_cheese == 'Y' :
        final_cost += extra_cheese
    print (f"Your final bill is ${final_cost}")\
        
else:
  pass