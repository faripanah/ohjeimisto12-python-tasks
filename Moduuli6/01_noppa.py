import random

def silmaluku():
    x = random.randint(1,6)
    return x

summa = 0  #muuttuja, joka laskee heittokerrat
luku = 0   #muuttuja, joka säilyttää silmaluvun 

while luku != 6:
    luku = silmaluku()
    summa += 1
    print("Heittä nopan kunnes tulee kuutonen.")

print(f"{summa} kerran heiton jälkeen tuli kuutonen.")
   
