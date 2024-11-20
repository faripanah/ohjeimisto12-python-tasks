from auto import Polttomoottoriauto
from auto import  Sähköauto

auto1 = Polttomoottoriauto("ACD-123", 165 , 32.3 )
auto2 = Sähköauto ("ABC-15", 180 , 52.5 )

# Aseta nopeudet
auto2.kiihdytä(100)
auto1.kiihdytä(120)


auto1.kulje(3)
auto2.kulje(3)
print(f"Sähköauton ({auto2.rekisteritunnus}) matkamittarilukema: {auto2.x} km")
print(f"Polttomoottoriauton ({auto1.rekisteritunnus}) matkamittarilukema: {auto1.x} km")
