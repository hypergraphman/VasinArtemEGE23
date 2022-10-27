from itertools import permutations

alf = 'kapkan'
s = set()
for word in permutations(alf):
    word = ''.join(word)
    if not ('kk' in word or 'aa' in word):
        s.add(word)
print(len(s))