import numpy as np
#Edabit N-Sized Parts
def partition(txt, n):
    #print(txt[0:2], txt[2:4])
    lst = []
    for i in range(0, len(txt), n):
        lst.append(txt[i: i + n])
    return lst
print(partition("chew", 2))

ar = np.ones((3,2))
print(ar.ndim)