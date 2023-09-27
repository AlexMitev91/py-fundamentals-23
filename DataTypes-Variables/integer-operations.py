total = 0

for i in range(4):
    input_num = int(input())
    if i < 2:
        total += input_num
    elif i == 2:
        total = total // input_num
    elif i == 3:
        total = total * input_num

print(total)

