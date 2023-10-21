neighborhood = list(map(int, input().split("@")))

current_postion = 0

while True:
    command = input().split()
    if command[0] == "Love!":
        break

    jump_location = int(command[1]) + current_postion
    current_postion = jump_location

    if current_postion > (len(neighborhood) -1):
        current_postion = 0

    if neighborhood[current_postion] <= 0:
        print(f"Place {current_postion} already had Valentine's day.")
        continue

    neighborhood[current_postion] -= 2
    
    if neighborhood[current_postion] <= 0:
        print(f"Place {current_postion} has Valentine's day.")

print(f"Cupid's last position was {current_postion}.")

if sum(neighborhood) <= 0:
    print("Mission was successful.")
else: 
    failed_counter = 0
    for house in neighborhood:
        if house > 0:
            failed_counter += 1
    print(f"Cupid has failed {failed_counter} places.")

