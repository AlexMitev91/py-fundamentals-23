from math import ceil

students_number = int(input())
lectures_number = int(input())
additional_bonus = int(input())

best_student = 0
best_student_attendences = 0

for student in range(1, students_number +1):
    student_attendances = int(input())
    current_student = student_attendances / lectures_number * (5 + additional_bonus)
    if current_student > best_student:
        best_student = current_student
        best_student_attendences = student_attendances

print(f"Max Bonus: {ceil(best_student)}.")
print(f"The student has attended {ceil(best_student_attendences)} lectures.")