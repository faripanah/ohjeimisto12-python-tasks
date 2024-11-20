class Julkaisu:
    def __init__(self, nimi) :
        self.nimi = nimi

    def tulosta_tiedot(self):
        print(f"{self.nimi}")


class Kirja(Julkaisu):
    def __init__(self, nimi, kirjoittaja, maara):
        super().__init__(nimi)
        self.kirjoittaja_nimi = kirjoittaja
        self.sivu_maara = maara

    def tulosta_tiedot(self):
        super().tulosta_tiedot()
        print(f"Kirjailija {self.kirjoittaja_nimi}, sivu {self.sivu_maara}")
