# 11/19/2019 or November 19, 2019 - 19/11/2019
# 7/26/2019 - 26/7/2019
from datetime import datetime

# df = ['01/31/2014', '02/06/2013']    
# f = [dtime.strptime(d, "%m/%d/%Y").strftime("%d/%m/%Y") for d in df]
def convert(d):
    monthsNum = [x for x in range(1,13)]
    # number month format
    if d[:d.find('/')] in str(monthsNum):
        converted = datetime.strptime(d, "%m/%d/%Y").strftime("%d/%m/%Y")
        return converted[:5].replace('0', '', 2) + converted[5:]

    # word month format
    else:
        months = ('January', 'February', 'March', 'April', 'May', 'June',
                'July', 'August', 'September', 'October', 'November', 'December')
        dic = dict(zip(months, monthsNum))
        for keys, values in dic.items():
            if keys in d:
                d = d.replace(keys, str(values)).replace(",", ' ')
                converted = datetime.strptime(d, "%m %d %Y").strftime("%d/%m/%Y")
                return converted[:5].replace('0', '', 2) + converted[5:]
    

print(convert('11/19/2019'), '19/11/2019')
print(convert('November 19, 2019'), '19/11/2019')
print(convert('1/1/2019'), '1/1/2019')
print(convert('January 1, 2019'), '1/1/2019')

