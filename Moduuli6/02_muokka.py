
import random

# Funktio, joka palauttaa satunnaisen silmäluvun väliltä 1..max_silmaluku
def silmaluku(tahkojen_maara):
    return random.randint(1, tahkojen_maara)

# Kysytään käyttäjältä nopan tahkojen määrä
tahkojen_maara = int(input("Anna nopan tahkojen määrä: "))

maksimi_silmaluku = tahkojen_maara
summa = 0  # Heittojen laskuri
luku = 0   # Alustetaan muuttuja, joka säilyttää silmäluvun

# Heitetään noppaa, kunnes saadaan maksimisilmäluku
while luku != maksimi_silmaluku:
    luku = silmaluku(tahkojen_maara)
    summa += 1
    print(f"Heitetty silmäluku: {luku}")

print(f"{summa} heiton jälkeen tuli {maksimi_silmaluku}.")
