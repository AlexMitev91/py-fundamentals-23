words = input().split()
palindrome_check = input()

palindromes = []

for word in words: 
    if word == ''.join(reversed(word)):
        palindromes.append(word)

print(palindromes)
print(f"Found palindrome {palindromes.count(palindrome_check)} times")