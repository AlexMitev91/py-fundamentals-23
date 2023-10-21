food_quantity = float(input())
hay_quantity = float(input())
cover_quantity = float(input())
guineas_weight = float(input())

success = True

for day in range(1, 31):
    food_quantity -= 0.3
    if food_quantity <= 0:
        success = False
        break
    if day % 2 == 0:
        hay_quantity -= (food_quantity * 0.05)
        if hay_quantity <= 0:
            success = False
            break
    if day % 3 == 0:
        cover_quantity -= (guineas_weight / 3)
        if cover_quantity <= 0:
            success = False
            break

if success:
    print(f"Everything is fine! Puppy is happy! Food: {food_quantity:.2f}, Hay: {hay_quantity:.2f}, Cover: {cover_quantity:.2f}.")
else:
    print("Merry must go to the pet store!")