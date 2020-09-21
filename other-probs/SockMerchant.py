def sockMerchant(n, ar):
    counter = 0
    for i in ar:
        # print(i, end =' ')
        if i == ar[i]:
            counter += 1
    print(counter)

sockMerchant(9, [10, 20, 20, 10, 30, 50, 10, 20])