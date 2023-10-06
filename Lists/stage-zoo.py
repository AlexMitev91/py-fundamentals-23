tail_str = str(input())
body_str = str(input())
head_str = str(input())

normal_body = []

for i in range(3):
    if i == 0:
        normal_body.append(head_str)
    elif i == 1:
        normal_body.append(body_str)
    else:
        normal_body.append(tail_str)

print(normal_body)