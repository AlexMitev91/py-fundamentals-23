def aliquot (num):
    is_perfect = False
    total = 0
    for i in range(1, num):
        positive_divisor = (num / i)
        if positive_divisor % 1 == 0:
            total += i
    if total == num:
        is_perfect = True
    return is_perfect    

number = int(input())

if aliquot(number):
    print("We have a perfect number!")
else:
    print("It's not so perfect.")


