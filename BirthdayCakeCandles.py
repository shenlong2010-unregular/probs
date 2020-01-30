# HackerRank Birthday Cake Candles
def birthdayCakeCandles(num_candles, arr):
    counter = 0
    # count the largest number in the arr
    for i in arr:
        if i == max(arr):
            counter += 1
    return(counter)
print(birthdayCakeCandles(4, [3, 2, 1, 3, 5, 5, 99]))