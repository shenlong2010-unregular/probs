# n = [int(input()) for _ in range(6)]
n = [100, 200, 300, 150, 250, 350]
lst = []
s = ('Pop', 'Snap','Crackle')
for i in n:
    if i % 3 == 0:
        lst.append(s[0])
    elif i % 3 != 0 and i % 2 != 0:
        lst.append(s[1])
    elif i % 3 != 0 and i % 2 == 0:
        lst.append(s[2])

print(' '.join(lst))