# Edabit Array Difference
def array_diff(a,b):
    # empty list to store
    lst = []
    
    # loop through list a and check if x not in b list
    # return new list where a[value] not in b[value] 
    for x in a:
        if x not in b:
            lst.append(x)
    return lst

print(array_diff([1,2,2], [1]))