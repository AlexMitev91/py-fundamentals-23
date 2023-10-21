bitcoin = 0
health = 100
best_room = 0

dungeon_map = input().split("|")

cleared_run = True
for room in dungeon_map:
    best_room += 1
    command = room.split()
    action = command[0]
    number = int(command[1])

    if action == "potion":
        temp_health = int(health)
        health += number
        if health > 100:
            health = 100
        ammount_healed = health - temp_health
        print(f"You healed for {ammount_healed} hp.")
        print(f"Current health: {health} hp.")
    elif action == "chest":
        bitcoin += number
        print(f"You found {number} bitcoins.")
    else:
        monster = command[0]
        health -= number
        if health > 0:
            print(f"You slayed {monster}.")
        else:
            cleared_run = False
            print(f"You died! Killed by {monster}.")
            print(f"Best room: {best_room}")
            break

if cleared_run:
    print(f"You've made it!\nBitcoins: {bitcoin}\nHealth: {health}")


    

