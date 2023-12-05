student_scores=input("input a list of student score: ").split()
for n in range(0, len(student_scores)):
    student_scores[n]=int(student_scores[n])
highest_score=0    
for value in student_scores:
        if highest_score < value:
              highest_score=value
print(f"The highest score in the class is: {highest_score}")

