def characters_between_chars(char1, char2):
    char1_code = ord(char1)
    char2_code = ord(char2)

    if char1_code > char2_code:
        char1, char2 = char2, char1
        char1_code, char2_code = char2_code, char1_code

    result = ' '.join(chr(code) for code in range(char1_code + 1, char2_code))

    return result

char1 = input()
char2 = input()

result = characters_between_chars(char1, char2)
print(result)
