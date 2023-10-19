def add_piece(collection, piece, composer, key):
    if piece not in collection:
        collection[piece] = {"composer": composer, "key": key}
        print(f"{piece} by {composer} in {key} added to the collection!")
    else:
        print(f"{piece} is already in the collection!")

def remove_piece(collection, piece):
    if piece in collection:
        del collection[piece]
        print(f"Successfully removed {piece}!")
    else:
        print(f"Invalid operation! {piece} does not exist in the collection.")

def change_key(collection, piece, new_key):
    if piece in collection:
        collection[piece]["key"] = new_key
        print(f"Changed the key of {piece} to {new_key}!")
    else:
        print(f"Invalid operation! {piece} does not exist in the collection.")

def main():
    n = int(input())
    collection = {}

    for _ in range(n):
        piece_info = input().split("|")
        piece, composer, key = piece_info
        collection[piece] = {"composer": composer, "key": key}

    command = input()
    while command != "Stop":
        command_parts = command.split("|")
        action = command_parts[0]
        piece = command_parts[1]

        if action == "Add":
            composer = command_parts[2]
            key = command_parts[3]
            add_piece(collection, piece, composer, key)
        elif action == "Remove":
            remove_piece(collection, piece)
        elif action == "ChangeKey":
            new_key = command_parts[2]
            change_key(collection, piece, new_key)

        command = input()

    for piece, info in collection.items():
        print(f"{piece} -> Composer: {info['composer']}, Key: {info['key']}")

main()
