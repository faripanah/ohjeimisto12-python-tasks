
luku = int(input("Anna kokonaisluku: "))

on_alkuluku = True

if luku < 2:
    on_alkuluku = False
elif luku == 2:
    on_alkuluku = True  # 2 on alkuluku
elif luku % 2 == 0:
    on_alkuluku = False  # Parilliset luvut (paitsi 2) eivät ole alkulukuja
else:
    # Tarkistetaan  luvusta 3 alkaen
    for i in range(3, int(luku**0.5) + 1, 2):
        if luku % i == 0:
            on_alkuluku = False
            break

# Tulostetaan tulos
if on_alkuluku:
    print(f"Luku {luku} on alkuluku.")
else:
    print(f"Luku {luku} ei ole alkuluku.")
