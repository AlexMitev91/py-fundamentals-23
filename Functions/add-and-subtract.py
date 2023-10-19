def sum_numbers(a, b):
    result = a + b
    return result

def subtract(a, b):
    result = a - b
    return result


a = int(input())
b = int(input())
c = int(input())

x = sum_numbers(a, b)
x = subtract(x, c)

print(x)