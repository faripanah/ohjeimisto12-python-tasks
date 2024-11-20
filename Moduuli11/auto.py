class Auto:
    def __init__(self, rekisteritunnus, huippunopeus, v= 0, x = 0) :
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.v= v
        self.x = x
    def kiihdytä(self,nopeusmuutos):
        self.v+=nopeusmuutos
        if self.v > self.huippunopeus:
            print("auton nopeus ei saa kasvaa huippunopeutta suurimaksi!")
        elif self.v <0 :
            self.v = 0
            print("nopeusta ei saa olla negatiivinen!")
        else:
            print(f"auton nopeus on nyt {self.v} km/h")

    def kulje(self, tuntimäärä):
        kuljettu_matka = self.v * tuntimäärä
        self.x += kuljettu_matka


class Sähköauto(Auto):
    def __init__(self, rekisteritunnus, huippunopeus, akku, v=0, x=0):
        super().__init__(rekisteritunnus, huippunopeus, v, x)
        self.akkukapasiteetti = akku




class Polttomoottoriauto(Auto):
    def __init__(self, rekisteritunnus, huippunopeus, benza,v=0, x=0):
        super().__init__(rekisteritunnus, huippunopeus, v, x)
        self.benzatankki_koko = benza
        
