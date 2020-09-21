# Hackerank Mini-Max Sum
def miniMaxSum(arr):
    max_total = min_total = 0
    arr.sort()
    for i in arr:
##        print(i, end = " ")
        max_total = arr[1:len(arr)+1]
        min_total = arr[0:len(arr)-1]
    print(sum(min_total), end=' ')
    print(sum(max_total))
        
        

miniMaxSum([5,2,5,6,1])