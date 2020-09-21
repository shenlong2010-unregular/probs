n = [int(x) for x in input().split()]
foundEven = False
index = 0
lst = []
strNum = ''
while not foundEven and index < len(n):
    if n[index] % 2 == 0:
        lst.append(n[index])
        if len(n) == index:
            foundEven = True
    else:
        foundEven = False
    index += 1
print(' '.join(str(x) for x in lst))
print(' '.join(map(str, lst)))

for num in range(len(n)):
    if n[num] % 2 == 0:
        strNum += str(n[num]) + ' '
print(strNum.rstrip())
