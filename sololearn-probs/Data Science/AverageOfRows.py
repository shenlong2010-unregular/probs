import numpy as np

# First line: two integers separated by spaces
# the first indicates the rows of matrix X(n) and
# the second indicates the columns of X(p)
# Next n lines: values of the row in X
n, p = [int(x) for x in input().split()]
X = []
# # valeus of the row X according to the number of n we have - n is rows
for i in range(n):
    X.append([float(x) for x in input().split()])

arr = np.array(X)
# print(arr.shape)
arr = np.around(arr, decimals = 2)
arr = arr.reshape(n,p)
print(arr.mean(axis=1).round(2)) # row mean with axis 1, column mean with axis 0
    