import random

class Auto:
    def __init__(self, tunnus, huippunopeus):
        self.rekisteritunnus = tunnus
        self.huippunopeus = huippunopeus
        self.nykyinen_nopeus = 0
        self.kuljettu_matka = 0

    
    def kiihdytä(self,nopeusmuutos):
        self.nykyinen_nopeus += nopeusmuutos
        if self.nykyinen_nopeus > self.huippunopeus:
            print("auton nopeus ei saa kasvaa huippunopeutta suurimaksi!")
        elif self.nykyinen_nopeus <0 :
            
            print("nopeusta ei saa olla negatiivinen!")
            self.nykyinen_nopeus = 0
        else:
            print(f"auton nopeus on nyt {self.nykyinen_nopeus} km/h")


    def kulje(self, tuntimäärä):
        self.kuljettu_matka += self.nykyinen_nopeus * tuntimäärä

