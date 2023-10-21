sequence = list(map(int, input().split()))

shot_targes = []
while True:
    command = input()
    if command == "End":
        break
    index = int(command)

    if 0 <= index <= (len(sequence) -1):
        if sequence[index] == -1:
            continue
        temp_item = sequence[index]
        sequence[index] = -1

        for item in range(len(sequence)):
            if sequence[item] > temp_item and sequence[item] > 0:
                sequence[item] -= temp_item
            elif sequence[item] <= temp_item and sequence[item] > 0:
                sequence[item] += temp_item

for item in sequence:
    if item < 0:
        shot_targes.append(item)

formatted_sequence = ' '.join(map(str, sequence))
print(f"Shot targets: {len(shot_targes)} -> {formatted_sequence}")
            


