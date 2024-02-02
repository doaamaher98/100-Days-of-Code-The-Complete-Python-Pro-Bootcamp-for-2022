students_scores = input ("Input a list of students scores\n").split()

students_scores_num = len(students_scores)

highest_score = 0

for n in range(0,students_scores_num):
    students_scores[n] = int(students_scores[n])
    
    if highest_score < students_scores[n]:
        highest_score = students_scores[n]
    

print(f"Highest score is : {highest_score}")