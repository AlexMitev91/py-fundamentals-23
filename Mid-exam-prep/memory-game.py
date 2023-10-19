elements = list(map(str, input().split()))
moves = 0

while True:
    is_valid = True

    command = input().split()
    if command[0] == "end":
        print("Sorry you lose :(")
        print(f"{' '.join(map(str, elements))}")
        break

    moves += 1
    index1 = int(command[0])
    index2 = int(command[1])

    if index1 == index2\
        or index1 >= len(elements)\
        or index2 >= len(elements)\
        or index1 < 0\
        or index2 < 0:

        elements_mid = len(elements) // 2
        elements.insert(elements_mid, f'-{moves}a')
        elements.insert(elements_mid, f'-{moves}a')
        print("Invalid input! Adding additional elements to the board")
        is_valid = False

    if elements[index1] == elements[index2] and is_valid == True:
        print(f"Congrats! You have found matching elements - {elements[index1]}!")
        second_el = elements[index2]
        elements.pop(index1)
        elements.remove(second_el)

    elif elements[index1] != elements[index2] and is_valid == True:
        print("Try again!")
    
    if len(elements) == 0:
        print(f"You have won in {moves} turns!")
        break
