numbers = input().split()

numbers_list = [int(x) for x in numbers]

def is_even(x):
    if x % 2 != 0:
        return False
    else:
        return True 

result = list(filter(is_even, numbers_list))

print(result)