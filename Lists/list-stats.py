n = int(input())

positive_nums = []
negative_nums = []

count_positives = 0
sum_of_negatives = 0

for i in range(n):
    current_num = int(input())
    if current_num < 0:
        negative_nums.append(current_num)
        sum_of_negatives += current_num
    else:
        positive_nums.append(current_num)
        count_positives += 1

print(f"{positive_nums}\n{negative_nums}")
print(f"Count of positives: {count_positives}\nSum of negatives: {sum_of_negatives}")