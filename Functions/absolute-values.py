input_list = input().split()

absolute_values = []

for number in input_list:
    absolute_values.append(abs(float(number)))

print(absolute_values)