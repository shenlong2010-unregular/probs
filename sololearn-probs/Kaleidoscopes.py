k = 1
tax, discount = (0.07, 0.1)
item = total = 0
if k == 1:
    total = k * 5.00
    tax *= total
    print('%.2f' % (total + tax))
else:
    total = k * 5.00
    discount *= total
    tax *= (total - discount)
    print('{:.2f}'.format(total - discount + tax))