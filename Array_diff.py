def array_diff(a,b):
    lst = []
    for x in a:
        if x not in b:
            lst.append(x)
    return lst

print(array_diff([1,2,2], [1]))