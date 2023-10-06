losses = int(input())
helmet_price = float(input())
sword_price = float(input())
shield_price = float(input())
armor_price = float(input())

total_expense = 0
broken_shields = 0
for current_fight in range(1, losses + 1):
    if current_fight % 2 == 0: 
        total_expense += helmet_price
    if current_fight % 3 == 0:
        total_expense += sword_price
        if current_fight % 2 == 0:
            total_expense += shield_price
            broken_shields += 1
            if broken_shields % 2 == 0:
                total_expense += armor_price

print(f"Gladiator expenses: {total_expense:.2f} aureus")
    


