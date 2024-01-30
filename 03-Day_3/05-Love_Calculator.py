print ("Welcome to the Love Calculator!")

name1 = input ("What is your name? \n")
name2 = input ("What is their name? \n")

# .lower() , .upper()
# .count('char') , where char is case sensitive
name1_lower = name1.lower()
name2_lower = name2.lower()

# We have to find out how many times "TRUE" and "LOVE" either in lower or uppper cases
TRUE_count_n1 = 0
TRUE_count_n2 = 0

LOVE_count_n1 = 0
LOVE_count_n2 = 0

# True count
TRUE_count_n1 = int (name1_lower.count('t') + name1_lower.count('r') + name1_lower.count('u') + name1_lower.count('e'))
TRUE_count_n2 = int (name2_lower.count('t') + name2_lower.count('r') + name2_lower.count('u') + name2_lower.count('e'))
Total_TRUE_count = TRUE_count_n1 + TRUE_count_n2

# Love count
LOVE_count_n1 = int (name1_lower.count('l') + name1_lower.count('o') + name1_lower.count('v') + name1_lower.count('e'))
LOVE_count_n2 = int (name2_lower.count('l') + name2_lower.count('o') + name2_lower.count('v') + name2_lower.count('e'))
TOTAL_LOVE_count = LOVE_count_n1 + LOVE_count_n2

Final_Love_Score        = str(Total_TRUE_count) + str(TOTAL_LOVE_count)
Final_Love_Score_int    = int(Final_Love_Score)

# print (f"Your score is {Final_Love_Score_int}%")

if Final_Love_Score_int < 10 or Final_Love_Score_int > 90 :
    print (f"Your score is {Final_Love_Score_int}, you go together like coke and mentos")
elif Final_Love_Score_int >= 40 and Final_Love_Score_int <= 50 :
    print(f"Your score is {Final_Love_Score_int}, you are alright together")
else :
    print(f"Your score is {Final_Love_Score_int}%")