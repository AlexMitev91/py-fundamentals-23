total_coffees = 0

while True:
    event = input()

    if event == "END":
        break

    if event.lower() == "cat" \
        or event.lower() == "dog" \
        or event.lower() == "coding" \
        or event.lower() == "movie":
        if event.islower():
            total_coffees += 1
        else:
            total_coffees += 2 

    if total_coffees > 5:
        print("You need extra sleep")
        break

if total_coffees <= 5:
    print(total_coffees)