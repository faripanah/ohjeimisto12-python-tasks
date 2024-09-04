def func(l_luku):
    summa = 0
    for i in l_luku:
        summa += i
    return summa


list_lukuja = [3,4,8,10,2,6]
lukuja_summa = func(list_lukuja)
print(lukuja_summa)