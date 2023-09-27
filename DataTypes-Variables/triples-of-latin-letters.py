input_number = int(input())

for first_symbol in range(input_number):
    for second_symbol in range(input_number):
        for third_symbol in range(input_number):
            print(f"{chr(97 + first_symbol)}{chr(97 + second_symbol)}{chr(97 + third_symbol)}")