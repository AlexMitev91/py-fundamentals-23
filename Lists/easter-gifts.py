gifts_list = str(input()).split()

while True:
    current_command = str(input()).split()

    break_checker = ' '.join(map(str,current_command))

    if break_checker == "No Money":
        break

    if current_command[0] == "OutOfStock":
        for i in range(len(gifts_list)):
            if gifts_list[i] == current_command[1]:
                gifts_list[i] = "None"

    elif current_command[0] == "Required":
        for i in range(len(gifts_list)):
            if i == int(current_command[2]):
                gifts_list[i] = current_command[1]

    elif current_command[0] == "JustInCase":
        gifts_list[-1] = current_command[1]

while "None" in gifts_list:
    gifts_list.remove("None")

print(*gifts_list, sep = " ")