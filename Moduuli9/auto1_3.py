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
       

auto = Auto("ABC-123", 142)
print(f"auton rekisteritunnuksen on {auto.rekisteritunnus} ja sen huippunopeus on {auto.huippunopeus}")
print(f"auton tämänhetkinen nopeus on {auto.v} ja kuljettu matka on {auto.x}")
auto.kiihdytä(30)
auto.kiihdytä(70)
auto.kiihdytä(50)
print(f"auton nopeuden on {auto.v} km/h")
auto.kiihdytä(-200)
print(f"auton nopeuden on {auto.v} km/h")
auto.x = 2000
auto.v = 60
auto.kulje(1.5)
print(f"kuljetun matkan lukemaan on {auto.x} km")
