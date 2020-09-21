menu = {
    'Nachos': 6,
    'Pizza': 6,
    'Cheeseburger': 10,
    'Water': 4,
    'Coke': 5
}

total = 0
items = 'Cheeseburger Cheeseburger Coke Water'
for item in items.split():
    if item in menu:
        total += menu.get(item, item)
    else:
        total += menu['Coke']
tax = 0.07 * total 
print(total + tax)