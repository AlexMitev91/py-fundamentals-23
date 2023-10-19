initial_inventory = input().split(", ")

while True:
    current_item = input().split(" - ")
    command = current_item[0]

    if command == "Craft!":
        break

    items = current_item[1]

    if command == "Collect":
        if items in initial_inventory:
            continue
        else:
            initial_inventory.append(items)
    if command == "Drop":
        if items in initial_inventory:
            initial_inventory.remove(items)
    if command == "Combine Items":
        replace_items = items.split(":")
        new_item = replace_items[1]
        old_item = replace_items[0]
        if old_item in initial_inventory:
            old_location = initial_inventory.index(old_item)
            initial_inventory.insert(old_location +1, new_item)
    if command == "Renew":
        if items in initial_inventory:
            old_location = initial_inventory.index(items)
            initial_inventory.append(items)
            initial_inventory.pop(old_location)

formatted_string = ', '.join(map(str, initial_inventory))

print(formatted_string)



