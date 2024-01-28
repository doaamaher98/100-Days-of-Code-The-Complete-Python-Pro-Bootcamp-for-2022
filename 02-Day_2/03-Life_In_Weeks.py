##########################################
# Calculate the time left until reaching
# 90 y/o
##########################################

current_age = input("What is your current age ?\n")

reference_age = 90

# 1 year = 365 days
#        = 52 weeks
#        = 12 months

years_left = 90 - int(current_age)

months_left = years_left * 12
weeks_left  = years_left * 52
days_left   = years_left * 365

print(f"You have {days_left} days, {weeks_left} weeks and {months_left} months left")
