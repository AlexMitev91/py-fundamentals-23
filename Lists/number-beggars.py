stuff_string = input().split(", ")
beggars = int(input())
stuff_int = []

for stuff in stuff_string:
    stuff_int.append(int(stuff))

beggars_collection = []
start_index = 0

while start_index < beggars:
    current_beggar = 0
    for current_index in range(start_index, len(stuff_int), beggars):
        current_beggar += stuff_int[current_index]
    beggars_collection.append(current_beggar)
    start_index += 1
print(beggars_collection)
