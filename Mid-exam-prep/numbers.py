numbers = list(map(int, input().split()))

average_num = sum(numbers) / len(numbers)

greater_than_avg = []

top_five = []
top_count = 5

for number in numbers:
    if number > average_num:
        greater_than_avg.append(number)

if len(greater_than_avg) < top_count:
    top_count = len(greater_than_avg)

if len(greater_than_avg) > 0:
    for number in range(top_count):
        top_five.append(max(greater_than_avg))
        greater_than_avg.remove(max(greater_than_avg))

    formatted_string = ' '.join(map(str, top_five))
    print(formatted_string)

else:
    print("No")