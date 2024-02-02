students_heights = input ("Input a list of student heights\n").split()

sum = 0
average = 0

students_number = len(students_heights) 

for n in range(0, students_number):
    students_heights[n] = int(students_heights[n])
    sum += students_heights[n] 

average = float(sum / students_number)

print(f"Average is : {round(average)}")