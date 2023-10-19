def grading_system(a):
    if 2.00 <= a <= 2.99:
        return 'Fail'
    elif 3.00 <= a <= 3.49:
        return 'Poor'
    elif 3.50 <= a <= 4.49:
        return 'Good'
    elif 4.50 <= a <= 5.49:
        return 'Very Good'
    elif 5.50 <= a <= 6.00:
        return 'Excellent'
    else:
        return 'Invalid grade! Grade must be between 2.00 and 6.00'

grade = float(input())

print(f"{grading_system(grade)}")

