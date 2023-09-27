n = int(input())

total_price = 0

for i in range(n):
    order_price = float(input())
    days = int(input())
    capsules = int(input())

    if order_price < 0.01 or order_price > 100.00:
        continue
    elif days < 1 or days > 31:
        continue
    elif capsules < 1 or capsules > 2000: 
        continue
    
    order_total = abs(order_price * (capsules * days))

    print(f"The price for the coffee is: ${order_total:.2f}")

    total_price += order_total

print(f"Total: ${abs(total_price):.2f}")