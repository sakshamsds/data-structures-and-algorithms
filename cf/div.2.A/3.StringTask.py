

s = input().lower()

vowels = ['a', 'e', 'i', 'o', 'u', 'y']

res = []
for chr in s:
    if chr not in vowels:
        res.append('.')
        res.append(chr)

print(''.join(res))