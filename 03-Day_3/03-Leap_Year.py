year = int(input ("Enter the Year to determine if its a leap year or not :\n"))

# Leap year if its divisible by 4 evenly
# EXCEPT if its evenly divisible by 100, its not leap year
# UNLESS if its evenly divisible by 400, its a leap year

if year % 4 == 0 :
    if year % 100 == 0:
        if year % 400 == 0 :
            print("This is a leap year")
        else :
            print("This is not a leap year")
    else :
            print("This is a leap year")

else :
    print("This is not a leap year")