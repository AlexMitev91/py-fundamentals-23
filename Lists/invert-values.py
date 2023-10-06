list_of_numbers = input().split()

inverted_list = []

for number in list_of_numbers:
    current_number = -int(number)
    inverted_list.append(current_number)
print(inverted_list)