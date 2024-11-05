from autokilpailu4 import Auto
from tabulate import tabulate
import random
autot = []
# for lause , jossa luodaan 10 autoa, jota lisätään listaan
for i in range(10):
    huippunopeus = random.randint(100, 200)
    autot.append(Auto(f"ABC-{i+1}", huippunopeus))
# kilpailu while loopissa , jatkuu kunnes jonkun auton matka>10000
# Kilpailu alkaa
kilpailu_kaynnissa = True
while kilpailu_kaynnissa:
    for auto in autot :
        #for auto in autot: arvotaan nopeus, kiihdytetään, kuljetaan 1h
        nopeuden_muutos = random.randint(-10, 15)
        auto.kiihdytä(nopeuden_muutos)
        auto.kulje(1)
        if auto.kuljettu_matka >= 10000:
            kilpailu_kaynnissa = False
            break
    
   
  
'''# tulostetaan autot, esim tabulata 
print(f"{'Rekisteritunnus ':<15}{' Huippunopeus':<15}{'Nykyinen nopeus':<20}{'Kuljettu matka':<15}")
print("-" * 65)
for auto in autot:
    print(f"{auto.rekisteritunnus :<15}{ auto.huippunopeus:<20}{auto.nykyinen_nopeus:<20}{auto.kuljettu_matka:<15.1f}")
'''
# Muodostetaan taulukko tabulate-tulostusta varten
data = []
for auto in autot:
    data.append({
        "Rekisteritunnus": auto.rekisteritunnus,
        "Huippunopeus (km/h)": auto.huippunopeus,
        "Nykyinen nopeus (km/h)": auto.nykyinen_nopeus,
        "Kuljettu matka (km)": f"{auto.kuljettu_matka:.1f}"
    })

# Tulostetaan tiedot taulukkona
print(tabulate(data, headers="keys", tablefmt="grid"))



