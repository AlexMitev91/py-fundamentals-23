initial_values = list(map(int, input().split()))

while True:
    command = input().split()
    action = command[0]
    if action == "end":
        break

    if action == "swap":
        index_1 = int(command[1])
        index_2 = int(command[2])
        temp_value = initial_values[index_1]
        initial_values[index_1] = initial_values[index_2]
        initial_values[index_2] = temp_value

    if action == "multiply":
        index_1 = int(command[1])
        index_2 = int(command[2])
        result = (int(initial_values[index_1]) * int(initial_values[index_2]))
        initial_values[index_1] = result

    if action == "decrease":
        for number in range(len(initial_values)):
            initial_values[number] -= 1

formatted_values = ', '.join(map(str, initial_values))

print(formatted_values)

