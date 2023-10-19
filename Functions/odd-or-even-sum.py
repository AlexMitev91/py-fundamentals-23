def even_sum (nums):
    total = 0
    for number in nums:
        if number % 2 == 0:
            total += number
    return total

def odd_sum (nums):
    total = 0
    for number in nums:
        if number % 2 != 0:
            total += number
    return total

number = input()
number_list = [int(x) for x in number]

even_result = even_sum(number_list)
odd_result = odd_sum(number_list)

print(f"Odd sum = {odd_result}, Even sum = {even_result}")
