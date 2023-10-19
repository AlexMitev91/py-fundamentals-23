total_price = 0
taxed_price = 0


special = False

while True:
    command = input()
    if command == "special":
        special = True
    if command == "special" or command == "regular":
        taxed_price *= 1.2
        break
    part_price = float(command)

    if part_price < 0:
        print("Invalid price!")
        continue
    else:
        total_price += part_price
        taxed_price += part_price

special_price = taxed_price * 0.9

if total_price > 0 and special == False:
    print("Congratulations you've just bought a new computer!")
    print(f"Price without taxes: {total_price:.2f}$")
    print(f"Taxes: {(taxed_price - total_price):.2f}$")
    print("-----------")
    print(f"Total price: {taxed_price:.2f}$")
elif total_price > 0 and special == True:
    print("Congratulations you've just bought a new computer!")
    print(f"Price without taxes: {total_price:.2f}$")
    print(f"Taxes: {(taxed_price - total_price):.2f}$")
    print("-----------")
    print(f"Total price: {special_price:.2f}$")
else:
    print("Invalid order!")