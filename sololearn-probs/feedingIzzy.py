f = {
    'Lettuce': 5,
    'Carrot': 4,
    'Mango': 9
}

s = 'Carrot Carrot Carrot'
p = 0

for i in s.split():
    if i in f:
        p += f.get(i, 0)
    
print(p)

