def palindrome (a):
    for number in a:
        reversed_num = number[::-1]
        if number == reversed_num:
            print("True")
        else:
            print("False")


a = input().split(", ")

palindrome(a)