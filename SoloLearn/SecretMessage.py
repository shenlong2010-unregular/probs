s = 'Hello World'.lower()
alphabet = []
for i in range(97, 123):
    alphabet.append(chr(i))
    
hash = dict(zip(alphabet, reversed(alphabet)))
new = ""
for i in s:
    new += hash.get(i, i)
print(new)
