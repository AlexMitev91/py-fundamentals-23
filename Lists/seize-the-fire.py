cells = input().split("#")
water = int(input())

effort = 0

seized_cells = []

total_fires = 0

for fire in cells:
    current_fire = fire.split(" = ")
    severity = current_fire[0]
    amount = int(current_fire[1])

    if severity == "High" and not 81 <= amount <= 125:
        continue
    elif severity == "Medium" and not 51 <= amount <= 80:
        continue
    elif severity == "Low" and not 1 <= amount <= 50:
        continue
    
    if (water - amount) >= 0:
        water -= amount
        effort += (amount * 0.25)
        total_fires += amount
        seized_cells.append(amount)
        if water <= 0:
            break
    elif (water - amount) < 0:
        continue


print("Cells:")
for item in seized_cells:
    print(f" - {item}")
print(f"Effort: {effort:.2f}")
print(f"Total Fire: {total_fires}")