'''
Create a function that takes the month and year (as integers) and
returns the number of days in that month.

days(2, 2018) ➞ 28

days(4, 654) ➞ 30

days(2, 200) ➞ 28

days(2, 1000) ➞ 28
'''
from calendar import monthrange
def day_amount1(month, year):
    return monthrange(year, month)[1]

def day_amount(month, year):
    if month in (1,3,5,7,8,10,12):
	    return 31
    elif month in (4,6,9,11):
        return 30
    else: # month == 2
        if any([year % 4 == 0 and not year % 100 == 0, year % 400 == 0 ]):
            return 29
        else:
            return 28

print(day_amount(2, 2011))
print(day_amount(2, 2012))
