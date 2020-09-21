def check_coupon(entered_code, correct_code, current_date, expiration_date):
    m1, d1, y1 = [x for x in current_date.split()]
    m2, d2, y2 = [x for x in expiration_date.split()]
    print(d1.split())
    # month_nums = [x for x in range(1, 13)]
    # month_words = [
    #     'January', 'February', 'March', 'April', 'May', 'June',
    #     'July', 'August', 'September', 'October', 'November','September' 
    # ]
    # months = dict(zip(month_words, month_nums))
    correct = True
    if str(entered_code) == str(correct_code) and m1 == m2 and d1 == d2 and y1 == y2:
                return correct
    return not correct

import datetime
def check_coupon1(entered_code, correct_code, current_date, expiration_date):
    if entered_code is correct_code:
        return (datetime.datetime.strptime(current_date, '%B %d, %Y')) <= (datetime.datetime.strptime(expiration_date, '%B %d, %Y'))
    return False
        
print(check_coupon1('123','123','September 4, 2014','September 3, 2014'))