# O(n) T | O(n) S
def moveElementToEnd(array, toMove):
    index = 0
    counter = 0
    lst = []
    while index < len(array):
        if array[index] != toMove:
            lst.append(array[index])
        else:
            counter += 1
        index += 1
    repeat = [str(toMove) * counter]
    lst.extend(map(int, ",".join(repeat)))
    return lst

print(moveElementToEnd([2, 1, 2, 2, 2, 3, 4, 2], 2))

def moveElementToEnd1(array, toMove):
    left = 0
    right = len(array) - 1
    