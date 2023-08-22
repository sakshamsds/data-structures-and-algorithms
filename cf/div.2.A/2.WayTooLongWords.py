
num_words = int(input())
for _ in range(num_words):
    word =  input()
    if len(word) <= 10:
        print(word)
    else:
        print(f'{word[0]}{len(word) - 2}{word[-1]}')