import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression

# number of data points in the feature matrix (n)
# n = int(input())

# X = []
# values of the row in the feature matrix, seperated by spaces
# for i in range(n):
#     X.append([float(x) for x in input().split()])

# target values separated by spaces
# y = [int(x) for x in input().split()]

# values (seperated by spaces) of a single datapoint without a target value
# datapoint = [float(x) for x in input().split()]

X = [[1.0, 3.0], [3.0, 5.0], [5.0, 7.0], [3.0, 1.0], [5.0, 3.0], [7.0, 5.0]] # feature
y = [1, 1, 1, 0, 0, 0] # target
datapoint = [2.0, 4.0] # single data point

model = LogisticRegression(solver='liblinear')
model.fit(X, y)
# print(model.predict(X))
# print(model.predict([datapoint]))
print(int(model.predict([datapoint])))
# print(model.coef_, model.intercept_) # [[-0.88029644  0.88029644]] [0.] => 0 = -0.88029644 + 0.88029644 + 0