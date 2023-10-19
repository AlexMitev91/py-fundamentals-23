wagons = [0] * int(input())

while True: 
    command = input().split()
    action = command[0]

    if action == "End":
        print(wagons)
        break  

    if action == "add":
        number_of_ppl = int(command[1])
        wagons[-1] += number_of_ppl
    if action == "insert":
        number_of_ppl = int(command[2])
        wagons[int(command[1])] += number_of_ppl
    if action == "leave":
        number_of_ppl = int(command[2])
        wagons[int(command[1])] -= number_of_ppl