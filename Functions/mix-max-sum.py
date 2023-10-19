a = input().split()
a = [int(x) for x in a]

minimum_number = min(a)
maximum_number = max(a)
sum_of_all_numbers = sum(a)

print(f"The minimum number is {minimum_number}")
print(f"The maximum number is {maximum_number}")
print(f"The sum number is: {sum_of_all_numbers}")