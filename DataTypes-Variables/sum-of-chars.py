n = int(input())

total_sum = 0

for i in range(n):
    character = ord(str(input()))
    total_sum += character

print(f"The sum equals: {total_sum}")
