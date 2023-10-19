a = input().split()
a = [int(x) for x in a]

x = sorted(a)

formatted_list = "[" + ", ".join(map(str, x)) + "]"

print(formatted_list)
