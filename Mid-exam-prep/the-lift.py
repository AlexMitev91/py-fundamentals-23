wait_line = int(input())
lift_state = list(map(int, input().split()))

for elevator in range(len(lift_state)):
    if (len(lift_state) * 4) - sum(lift_state) == 0:
        break
    if lift_state[elevator] >= 4:
        continue
    for people in range(wait_line):
        lift_state[elevator] += 1
        wait_line -= 1
        if lift_state[elevator] == 4:
            break

empty_spots = (len(lift_state) * 4) - sum(lift_state)
formatted_string = ' '.join(map(str, lift_state))

if empty_spots > 0 and wait_line == 0:
    print("The lift has empty spots!")
    print(f"{formatted_string}")
elif wait_line > 0 and empty_spots == 0:
    print(f"There isn't enough space! {wait_line} people in a queue!")
    print(f"{formatted_string}")
else:
    print(f"{formatted_string}")
