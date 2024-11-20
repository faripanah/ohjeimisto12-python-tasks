from autokilpailu4 import Auto
from tabulate import tabulate
import random
class Kilpailu:
    def __init__(self, nimi, pituus, autot) :
        self.kilpalu_nimi = nimi
        self.kilometrimärää= pituus
        self.autot = autot

    def tunti_kuluu(self):
        """ arpoo nopeuden muutokset ja päivittää jokaisen auton kuljetun matkan."""
        for auto in self.autot:
            nopeuden_muutos = random.randint(-10, 15)
            auto.kiihdytä(nopeuden_muutos)
            auto.kulje(1)

       


    def tulosta_tilanne(self):
     """Tulostaa kaikkien autojen tiedot taulukkomuodossa."""
    data = []
    for auto in self.autot:
          data.append({
              "Rekisteritunnus": auto.rekisteritunnus,
              "Huippunopeus (km/h)": auto.huippunopeus,
              "Nykyinen nopeus (km/h)": auto.nykyinen_nopeus,
              "Kuljettu matka (km)": f"{auto.kuljettu_matka:.1f}"
     })

# Tulostetaan tiedot taulukkona
    print(tabulate(data, headers="keys", tablefmt="grid"))


    def kilpailu_ohi(self):
        """Tarkistaa, onko kilpailu ohi, eli onko jokin auto saavuttanut kilpailun pituuden."""
        return any(auto.kuljettu_matka >= self.kilometrimaara for auto in self.autot)
       
       
