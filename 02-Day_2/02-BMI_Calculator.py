# Calculating the BMI value

height = float(input ("Enter your height in m : \n"))
weight = int(input ("Enter your weight in kg : \n"))

# BMI = weight/height^2

BMI_value = int (weight) / float(height**2)

BMI_int_value = int (BMI_value)

print(BMI_int_value)
##########################################
# Using round function
print (8/3)
print (round(8/3))
print (round(8/3, 2))

# Using floor divison to avoid the result to be float, but to be integer instead
print (8 // 3)

##########################################
# f-String
## This is used to avoid the type conversion in printing to str
score = 0
height = 1.4
isWinning = True

print ("Your score is " + str(score)) # Instead of doing this

## Use this way
print(f"Your score is {score}, your height is {height}")
##########################################

