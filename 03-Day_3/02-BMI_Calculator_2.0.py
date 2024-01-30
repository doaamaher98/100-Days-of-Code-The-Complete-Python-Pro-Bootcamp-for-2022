height = float(input ("Enter your height in m : \n"))
weight = float(input ("Enter your weight in kg : \n"))

# BMI = weight/height^2
BMI_value = round(weight / height**2,1)

print("Your BMI is "+ str(BMI_value))

# Checkings
if BMI_value < 18.5 :
    print(f"You are underweight with BMI : {BMI_value}")
elif BMI_value >= 18.5 and BMI_value < 25 :
    print(f"You have a normal weight with BMI : {BMI_value}")
elif BMI_value >= 25 and BMI_value < 30 :
    print(f"You are over weight with BMI : {BMI_value}")
elif BMI_value >= 30 and BMI_value < 35 :
    print(f"You are Obese with BMI : {BMI_value}")
else :
    print (f"You are Clinically Obese with BMI {BMI_value}")