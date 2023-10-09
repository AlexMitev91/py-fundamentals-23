full_collection = input().split("|")
budget = float(input())

initial_budget = budget
ticket_price = 150

bought_items = []
sold_items = []
profit = 0

clothes_max_price = 50.00
shoes_max_price = 35.00
accessories_max_price = 20.50


for item in full_collection:
    args = item.split("->")
    item_type = args[0]
    item_price = float(args[1])

    if item_type == "Clothes" and item_price > clothes_max_price:
        continue
    elif item_type == "Shoes" and item_price > shoes_max_price:
        continue
    elif item_type == "Accessories" and item_price > accessories_max_price:
        continue

    if item_price <= budget:
        budget -= item_price
        bought_items.append(item_price)
    elif item_price > budget:
        continue

for item in bought_items:
    item_profit = (float(item) * 1.4)
    profit += item_profit - float(item)
    sold_items.append(item_profit)


formatted_items = [f"{item:.2f}" for item in sold_items]

print(*formatted_items, sep = ' ')

print(f"Profit: {profit:.2f}")

if profit + initial_budget >= ticket_price:
    print("Hello, France!")
elif profit + initial_budget < ticket_price:
    print("Not enough money.")



