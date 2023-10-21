targets = list(map(int, input().split()))

while True: 
    command = input().split()

    if command[0] == "End":
        break

    action = command[0]
    index = int(command[1])
    value = int(command[2])

    if action == "Shoot":
        if 0 <= index < len(targets):
            targets[index] -= value
            if targets[index] <= 0:
                targets.pop(index)
    if action == "Add":
        if 0 <= index < len(targets):
            targets.insert(index, value)
        else:
            print(f"Invalid placement!")
    if action == "Strike":
        if (index - value) >= 0 and (index + value) < len(targets):
            start_index = index - value
            end_index = index + value
            del targets[start_index:end_index + 1]
        else:
            print(f"Strike missed!")

formatted_list = '|'.join(map(str, targets))
print(formatted_list)
