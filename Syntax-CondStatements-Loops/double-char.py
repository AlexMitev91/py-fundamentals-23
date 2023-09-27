while True:
    input_str = input().strip()

    if input_str == "End":
        break
    elif input_str == "SoftUni":
        continue

    doubled_str = ''.join(char * 2 for char in input_str)

    print(doubled_str)