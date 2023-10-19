def price_calculator(item, quantity):
    if item == 'coffee':
        return f'{1.50 * quantity:.2f}'
    elif item == 'water':
        return f'{1.00 * quantity:.2f}'
    elif item == 'coke':
        return f'{1.40 * quantity:.2f}'
    elif item == 'snacks':
        return f'{2.00 * quantity:.2f}'     
           
    # total_price = 0
    # if item == "coffee":
    #     total_price += (1.50 * quantity)
    # elif item == "water":
    #     total_price += (1.00 * quantity)
    # elif item == "coke":
    #     total_price += (1.40 * quantity)
    # elif item == "snacks":
    #     total_price += (1.20 * quantity)
    # return total_price

item = str(input())
quantity = int(input())

result = price_calculator(item, quantity)
print(result)
