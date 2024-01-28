##########################################
print ("Welcome to the tip calculator")

total_bill_str = input ("What was the total bill\n")
total_bill_float = float(total_bill_str)

tip_percentage_10 = 10
tip_percentage_12 = 12
tip_percentage_15 = 15

actual_tip_percentage = input (f"What percentage tip would you like to give {tip_percentage_10}, {tip_percentage_12} or {tip_percentage_15}\n")

over_all_tip = total_bill_float * (float(actual_tip_percentage)/100.0)

people_num = int(input ("How many people to split the bill ?\n"))

person_pay = (total_bill_float / people_num) + (over_all_tip / people_num)

print(f"Each person should pay : {round(person_pay,2)}")