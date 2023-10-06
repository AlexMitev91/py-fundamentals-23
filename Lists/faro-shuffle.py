deck = input().split()
shuffles = int(input())

for shuffle in range(shuffles):
    middle_deck = len(deck) // 2
    left_part = deck[0:middle_deck]
    righ_part = deck[middle_deck:]
    deck_afet_shuffle = []
    for current_index in range(len(left_part)):
        deck_afet_shuffle.append(left_part[current_index])
        deck_afet_shuffle.append(righ_part[current_index])
    deck = deck_afet_shuffle
print(deck)




