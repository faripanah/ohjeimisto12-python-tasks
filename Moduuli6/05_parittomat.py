def func(l_luku):
    pari_list = []
    for i in l_luku:
        if i%2 == 0:
            pari_list.append(i)
    return pari_list


list_lukuja = [3,4,8,10,2,6,7]
uusi_lista = func(list_lukuja)
print(list_lukuja)
print(uusi_lista)