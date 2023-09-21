n = int(input())

characters_to_check = [',', '.', '_']

for i in range(n):
    input_str = input().strip()

    if any(char in input_str for char in characters_to_check):
        print(f"{input_str} is not pure!")
    else:
        print(f"{input_str} is pure.")