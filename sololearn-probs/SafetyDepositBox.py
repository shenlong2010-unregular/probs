def time(items, take, time = 5):
    count = 1
    index = 0
    item = items.split(',')
    while index < len(item):
        if item[index] == take:
            break
        count += 1
        index += 1

    return count * time

def time1(items, take, time =5):
    c = 1
    for i in items.split(','):
        if i == take:
            break
        c += 1
    return c * time

print(time('gold,silver,jewels,cheese', 'gold'), 5)
print(time('gold,silver,jewels,cheese', 'silver'), 10)
print(time1('gold,silver,jewels,cheese', 'gold'), 5)
print(time1('gold,silver,jewels,cheese', 'silver'), 10)