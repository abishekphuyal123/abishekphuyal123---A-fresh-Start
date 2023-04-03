student_scores = {}
student_scores["Jack"] = 91
student_scores["Tom"] = 81
student_scores["David"] = 74
student_scores["Michael"] = 65

# Now, create a new dictionary named student_grades. 
student_grades = {}

for i in student_scores:
    score = student_scores[i]
    if student_scores[i] > 90:
        student_grades[i] = "Outstanding"
    elif student_scores[i] > 80:
        student_grades[i] = "Exceeded Expectations"
    elif student_scores[i] > 70:
        student_grades[i] = "Acceptable"
    else:
        student_grades[i] = "Fail. "


print(student_grades)