tank_capacity = 0

n = int(input())

for i in range(n):
    pour = int(input())
    tank_capacity += pour
    if tank_capacity > 255:
        tank_capacity -= pour
        print("Insufficient capacity!")
print(tank_capacity)
