initial_treasure = input().split("|")

while True:
    command = input().split()

    if command[0] == "Yohoho!":
        break

    action = command[0]

    if action == "Loot":
        for item in range(1, len(command)):
            if command[item] in initial_treasure:
                continue
            else:
                initial_treasure.insert(0, command[item])
    if action == "Drop":
        index = int(command[1])
        item = command[1]
        if 0 <= index <= len(initial_treasure):
            temp_item = initial_treasure[index]
            initial_treasure.pop(index)
            initial_treasure.append(temp_item)
    if action == "Steal":
        steal_count = int(command[1])
        stolen_treasures = []
        if steal_count > len(initial_treasure):
            steal_count = len(initial_treasure)
        for item in range(steal_count):
            stolen_treasures.append(initial_treasure[-1])
            initial_treasure.pop(-1)
        if len(stolen_treasures) > 0:
            formatted_string = ', '.join(map(str, reversed(stolen_treasures)))
            print(formatted_string)

treasure_count = 0
treasure_length = len(initial_treasure)

for item in initial_treasure:
    treasure_count += len(item)

if len(initial_treasure) > 0:
    print(f"Average treasure gain: {(treasure_count / treasure_length):.2f} pirate credits.")
else:
    print("Failed treasure hunt.")