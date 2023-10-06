first_string = input()
second_string = input()

last_printed = first_string

for char_index in range(len(first_string)):
    left_part = second_string[:char_index + 1]
    righ_part = first_string[char_index + 1:]

    new_string = left_part + righ_part

    if new_string == last_printed:
        continue
    print(new_string)
    last_printed = new_string