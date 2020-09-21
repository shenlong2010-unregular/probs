import math
def get_number_of_squares(n):
    if n <= 1:
        return 0
    sum = 1
    count = 1
    while sum < n:
        count += 1
        sum += count ** 2

    return count -1

print(get_number_of_squares(1), 0)
print(get_number_of_squares(2), 1)
print(get_number_of_squares(5), 1)
print(get_number_of_squares(6), 2)
print(get_number_of_squares(15), 3)