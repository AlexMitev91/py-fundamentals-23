import sys

num_input = input().split()
trim = int(input())

input_as_int = []

for number in num_input:
    input_as_int.append(int(number))

lowest_num = sys.maxsize

for current_num in range(trim):
    for i in range(len(input_as_int)):
        if input_as_int[i] < lowest_num:
            lowest_num = input_as_int[i]
    input_as_int.remove(lowest_num)
    lowest_num = sys.maxsize

print(*input_as_int, sep = ", ")
