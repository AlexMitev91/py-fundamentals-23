n = int(input())

numbers_list = []
curated_list = []

for i in range(n):
    number = int(input())
    numbers_list.append(number)

command = str(input())

if command == "even":
    for current_number in numbers_list:
        if current_number % 2 == 0:
            curated_list.append(current_number)
elif command == "odd":
    for current_number in numbers_list:
        if current_number % 2 != 0:
            curated_list.append(current_number)
elif command == "negative":
    for current_number in numbers_list:
        if current_number < 0:
            curated_list.append(current_number)
elif command == "positive":
    for current_number in numbers_list:
        if current_number >= 0:
            curated_list.append(current_number)
    
print(curated_list)
