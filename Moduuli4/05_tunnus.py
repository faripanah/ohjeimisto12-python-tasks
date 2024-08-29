# Oikeat käyttäjätunnus ja salasana
oikea_kayttajatunnus = "python"
oikea_salasana = "rules"

x = 0  

while x < 5:
    input_tunnus = input("Syötä käyttäjätunnus: ")
    input_salasana = input("Syötä salasana: ")
    
    if input_tunnus == oikea_kayttajatunnus and input_salasana == oikea_salasana:
        print("Tervetuloa!")
        break  
    else:
        print("Virheellinen käyttäjätunnus tai salasana.")
        x += 1  

if x == 5:
   print("Pääsy evätty.")


       

            