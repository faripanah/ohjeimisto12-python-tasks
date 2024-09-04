vuosiaja = "kevät", "kesä", "syksy", "talvi"
kuukausi_numero = int(input("Anna kuukauden numero (1-12): "))

if 3 <= kuukausi_numero <= 5:
    print(vuosiaja[0])  # Kevät
elif 6 <= kuukausi_numero <= 8:
    print(vuosiaja[1])  # Kesä
elif 9 <= kuukausi_numero <= 11:
    print(vuosiaja[2])  # Syksy
elif kuukausi_numero == 12 or 1 <= kuukausi_numero <= 2:
    print(vuosiaja[3])  # Talvi
else:
    print("Virheellinen kuukausi! Anna numero välillä 1-12.")
