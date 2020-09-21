#O(n^2 + m^2) Time | O(1) S
def smallestDifference(arrayOne, arrayTwo):
    difference = 0
    smallest = float("inf")

    lst = [0,0]
    for x in range(len(arrayOne)):
        for y in range(len(arrayTwo)):
            difference = abs(arrayOne[x] - arrayTwo[y])
            # print(smallest - difference)
            if difference < smallest:
                smallest = difference
                lst[0] = arrayOne[x]
                lst[1] = arrayTwo[y]
    return lst

#O(n^2 + m^2) Time | O(1) S
def smallestDifference1(arrayOne, arrayTwo):
    difference = 0
    smallest = float("inf")

    lst = [0,0]
    for x in arrayOne:
        for y in arrayTwo:
            difference = abs(x - y)
            # print(smallest - difference)
            if difference < smallest:
                smallest = difference
                lst[0] = x
                lst[1] = y
    return lst

print(smallestDifference([-1, 5, 10, 20, 28, 3], [26, 134, 135, 15, 17]))
print(smallestDifference1([-1, 5, 10, 20, 3], [26, 134, 135, 15, 17]))

#O(nlog(n) + mlog(m)) Time | O(1) S
def smallestDifference(arrayOne, arrayTwo):
    arrayOne.sort()
    arrayTwo.sort()
    idx1 = 0
    idx2 = 0
    
    smallest = float("inf") # infinity would be greater any number
    current = float("inf")
    smallestPair = []
    
    while idx1 < len(arrayOne) and idx2 < len(arrayTwo):
        firstNum = arrayOne[idx1]
        secondNum = arrayTwo[idx2]

        if firstNum < secondNum:
            current = secondNum - firstNum 
            idx1 += 1
        elif firstNum > secondNum:
            current = firstNum - secondNum
            idx2 += 1
        else:
            return [firstNum, secondNum]
        
        if smallest > current:
            smallest = current
            smallestPair = [firstNum, secondNum]
    return smallestPair
