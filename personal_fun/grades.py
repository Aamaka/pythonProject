grades = {
    "Harry":  81,
    "Ron": 78,
    "Hermione": 99,
    "Draco": 74,
    "Neville": 62
}

student_score = {}

for student in grades:
    score = grades[student]
    if score >= 91 <= 100:
        student_score[student] = "Outstanding"
    elif score >= 81 <= 90:
        student_score[student] = "Exceed Expectation"
    elif score >= 71 <= 80:
        student_score[student] = "Acceptable"
    else:
        student_score[student] = "Failed"
print(student_score)
