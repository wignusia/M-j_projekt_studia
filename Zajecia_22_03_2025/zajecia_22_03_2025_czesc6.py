length = 0
for x in range(4):
    word =input('POdaj słow')
    new_len= len(word)

if new_len<length:
    longest_word=word
    length=len(longest_word)

print(longest_word)
print('długośc słowa', length)