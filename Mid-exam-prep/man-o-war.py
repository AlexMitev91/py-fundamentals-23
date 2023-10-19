pirate_ship_status = list(map(int, input().split('>')))
warship_status = list(map(int, input().split('>')))

maximum_health_capacity = int(input())

game_won = False

while True:
    command = input().split()
    action = command[0]
    if action == "Retire":
        break

    if action == "Fire":
        index = int(command[1])
        damage = int(command[2])
        if 0 <= index < len(warship_status):
            warship_status[index] -= damage
            if warship_status[index] <= 0:
                print("You won! The enemy ship has sunken.")
                game_won = True
                break

    if action == "Defend":
        start_index = int(command[1])
        end_index = int(command[2])
        damage = int(command[3])
        if 0 <= start_index < len(pirate_ship_status) and 0 <= end_index < len(pirate_ship_status):
            for section in range(start_index, end_index + 1):
                pirate_ship_status[section] -= damage
                if pirate_ship_status[section] <= 0:
                    print("You lost! The pirate ship has sunken.")
                    game_won = True
                    break

    if action == "Repair":
        index = int(command[1])
        heal = int(command[2])
        if 0 <= index < len(pirate_ship_status):
             pirate_ship_status[index] += heal
             if pirate_ship_status[index] > maximum_health_capacity:
                pirate_ship_status[index] = maximum_health_capacity
                
    if action == "Status":
        counter = 0
        for section in range(len(pirate_ship_status)):
            if pirate_ship_status[section] < (maximum_health_capacity * 0.2):
                counter += 1
        print(f"{counter} sections need repair.")

if game_won == False:
    print(f"Pirate ship status: {sum(pirate_ship_status)}")
    print(f"Warship status: {sum(warship_status)}")
