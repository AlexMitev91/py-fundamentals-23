n = int(input())

current_ball = 0 

highest_value = 0

highest_weight = 0
highest_time = 0
highest_quality = 0

for snowballs in range(n):
    snowball_weight = int(input())
    snowball_time = int(input())
    snowball_quality = int(input())

    current_ball = (snowball_weight / snowball_time) ** snowball_quality

    if current_ball > highest_value:
        highest_value = current_ball
        highest_weight = snowball_weight
        highest_quality = snowball_quality
        highest_time = snowball_time


print(f"{highest_weight} : {highest_time} = {int(highest_value)} ({highest_quality})")