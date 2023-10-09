initial_energy = 100
initial_coin = 100

workday_events = input().split("|")
eod_energy = 100
coin_earned = 100

success = True

for event in workday_events:
    args = event.split("-")
    event_type = args[0]
    event_value = int(args[1])
    if event_type == "rest":
        current_energy = eod_energy
        eod_energy += event_value
        if eod_energy > 100:
            eod_energy = 100
        gained_energy = eod_energy - current_energy
        print(f"You gained {gained_energy} energy.")
        print(f"Current energy: {eod_energy}.")
    elif event_type == "order":
        if eod_energy >= 30:
            eod_energy -= 30
            coin_earned += event_value
            print(f"You earned {event_value} coins.")
        else:
            print(f"You had to rest!")
            eod_energy += 50
            if eod_energy > 100:
                eod_energy = 100
    else:
        if coin_earned >= event_value:
            coin_earned -= event_value
            print(f"You bought {event_type}.")
        else:
            print(f"Closed! Cannot afford {event_type}.")
            success = False
            break

if success:
    print(f"Day completed!\nCoins: {coin_earned}\nEnergy: {eod_energy}")
