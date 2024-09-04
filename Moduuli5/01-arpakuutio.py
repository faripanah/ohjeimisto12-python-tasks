lukumaara = int(input("Anna arpakuutioiden lukumäärä: "))

summa = 0 

for luku in range(lukumaara):
    silmaluku = random.randint(1, 6)  
    summa += silmaluku  

# Tulostetaan silmälukujen summa
print("Arpakuutioiden silmälukujen summa on:", summa)
