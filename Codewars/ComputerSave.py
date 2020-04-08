# O(n) Time | O(1) S
def save(sizes, hd):
    sum = 0
    count = len(sizes)
    for i in range(len(sizes)):
        sum += sizes[i]
        if sum > hd:
            count -= 1
            
    return count

print(save([4,4,4,3,3], 12))