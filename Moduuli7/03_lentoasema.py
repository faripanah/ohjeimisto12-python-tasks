# Luodaan tyhjät sanakirjat lentoasemien tallentamista varten
lentoasemat = {}

def syota_uusi_lentoasema():
    """Kysyy käyttäjältä uuden lentoaseman tiedot ja tallentaa ne sanakirjaan."""
    icao_koodi = input("Anna lentoaseman ICAO-koodi: ").strip().upper()
    nimi = input("Anna lentoaseman nimi: ").strip()
    lentoasemat[icao_koodi] = nimi
    print(f"Lentoasema {nimi} (ICAO: {icao_koodi}) on lisätty.")

def hae_lentoasema():
    """Kysyy käyttäjältä ICAO-koodin ja tulostaa vastaavan lentoaseman nimen."""
    icao_koodi = input("Anna lentoaseman ICAO-koodi: ").strip().upper()
    if icao_koodi in lentoasemat:
        print(f"Lentoasema ICAO-koodilla {icao_koodi} on {lentoasemat[icao_koodi]}.")
    else:
        print(f"Lentoasemaa ICAO-koodilla {icao_koodi} ei löydy.")

def main():
    """Ohjelman päätoiminto, joka tarjoaa valikon käyttäjälle."""
    while True:
        print("\nValitse toiminto:")
        print("1. Syötä uusi lentoasema")
        print("2. Hae lentoasema")
        print("3. Lopeta")
        
        valinta = input("Valintasi (1/2/3): ").strip()
        
        if valinta == "1":
            syota_uusi_lentoasema()
        elif valinta == "2":
            hae_lentoasema()
        elif valinta == "3":
            print("Ohjelma lopetetaan.")
            break
        else:
            print("Virheellinen valinta. Yritä uudelleen.")

# Suoritetaan ohjelma
main()
