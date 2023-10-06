n = int(input())
word_to_match = str(input())

all_words = []
for i in range(n):
    current_word = str(input())
    all_words.append(current_word)

for i in range(len(all_words) -1, -1, -1):
    element = all_words[i]
    if word_to_match not in element:
        all_words.remove(element)

print(all_words)