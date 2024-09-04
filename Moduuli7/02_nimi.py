nimi_set = set()
nimi = input("Syötä nimi: ")
while nimi != "":
   #nimi_set.add(nimi)
    if nimi in nimi_set:
        print("Aiemmin syötetty nimi")
    else:
        print("Uusi nimi")
        # Lisätään uusi nimi joukkoon
        nimi_set.add(nimi)
    nimi = input("Syötä nimi: ")


print("\nSyötetyt nimet:")
for nimi in nimi_set:
    print(nimi)

   