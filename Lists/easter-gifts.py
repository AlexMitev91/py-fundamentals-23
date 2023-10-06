gifts_string = str(input()).split()

gifts_list = []

for gift in gifts_string:
    gifts_list.append(gift)


while True:
    current_command = str(input()).split()

    if current_command[1] == "Money":
        break

    if current_command[0] == "OutOfStock":
        for i in range(len(gifts_list)):
            if gifts_list[i] == current_command[1]:
                gifts_list[i] = "None"

    elif current_command[0] == "Required":
        command_index = int(current_command[2])
        if command_index < len(gifts_list):
            gifts_list[command_index] = current_command[1]
        else:
            continue

    elif current_command[0] == "JustInCase":
        gifts_list[len(gifts_list)-1] = current_command[1]

while "None" in gifts_list:
    gifts_list.remove("None")

print(*gifts_list, sep = " ")


