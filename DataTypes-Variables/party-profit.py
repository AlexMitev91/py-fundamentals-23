from math import floor
group_size = int(input())
adv_days = int(input())

total_coins = 0

for i in range(1, adv_days +1):
    if (i % 10 == 0):
        group_size -= 2
    if (i % 15 == 0):
        group_size += 5
    if (i % 3 == 0):
        total_coins -= (group_size * 3)
    if (i % 5 == 0):
        total_coins += (group_size * 20)
        if (i % 3 == 0):
          total_coins -= (group_size * 2)
    total_coins += 50 
    total_coins -= (group_size * 2)

coins_per_adv = floor(total_coins / group_size)

print(f"{group_size} companions received {coins_per_adv} coins each.")