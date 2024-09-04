import math

def yksikkohinta(halk, hinta):
    # Laske pizzan säde metreinä (senttimetrit muutetaan metreiksi jakamalla 100:lla)
    sade = halk / 2 / 100
    # Laske pizzan pinta-ala (A = π * r^2)
    pinta_ala = math.pi * (sade ** 2)
    # Laske yksikköhinta (hinta per neliömetri)
    yks_hinta = hinta / pinta_ala
    return yks_hinta

# Pääohjelma
# Kysy käyttäjältä ensimmäisen pizzan halkaisija ja hinta
halkaisija1 = float(input("Anna ensimmäisen pizzan halkaisija (cm): "))
hinta1 = float(input("Anna ensimmäisen pizzan hinta (€): "))

# Kysy käyttäjältä toisen pizzan halkaisija ja hinta
halkaisija2 = float(input("Anna toisen pizzan halkaisija (cm): "))
hinta2 = float(input("Anna toisen pizzan hinta (€): "))

# Laske kummankin pizzan yksikköhinnat
yks_hinta1 = yksikkohinta(halkaisija1, hinta1)
yks_hinta2 = yksikkohinta(halkaisija2, hinta2)

# Ilmoita kumpi pizza antaa paremman vastineen rahalle
if yks_hinta1 < yks_hinta2:
    print("Ensimmäinen pizza antaa paremman vastineen rahalle.")
elif yks_hinta2 < yks_hinta1:
    print("Toinen pizza antaa paremman vastineen rahalle.")
else:
    print("Molemmat pizzat antavat saman vastineen rahalle.")

# Tulosta yksikköhinnat (valinnainen, mutta informatiivinen)
print(f"Ensimmäisen pizzan yksikköhinta on {yks_hinta1:.2f} €/m²")
print(f"Toisen pizzan yksikköhinta on {yks_hinta2:.2f} €/m²")

