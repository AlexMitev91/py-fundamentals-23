def rounding(str_input):
    list_of_numbers = []
    numbers = str_input.split()
    for number in numbers:
        rounded_number = round(float(number))
        list_of_numbers.append(rounded_number)
    return list_of_numbers

str_input = input()
formatted = rounding(str_input)
print(formatted)