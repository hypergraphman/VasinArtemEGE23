from itertools import product

alf = 'skola'
s = set()
for word in product(alf, repeat=3):
    word = ''.join(word)
    if word.count('k') == 1:
        s.add(word)
print(len(s))