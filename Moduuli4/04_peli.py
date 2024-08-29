import random

arpo_luku = random.randint(1,10)
arvaus = int(input("Arvaa luku väliltä 1..10: "))
while arvaus != arpo_luku:
    if arvaus < arpo_luku:
         print("Liian pieni arvaus.")
    elif arvaus > arpo_luku:
         print("Liian suuri arvaus.")
    else:
         print("Oikein!")
         break
    arvaus = int(input("Arvaa luku väliltä 1..10: "))
print("Good Job!!!!")
