
import random

# Kysytään käyttäjältä pisteiden määrä
pisteiden_maara = input("Anna arvottavien pisteiden määrä: ")

# Varmistetaan, että syöte on positiivinen kokonaisluku
if pisteiden_maara.isdigit():
    pisteiden_maara = int(pisteiden_maara)

    if pisteiden_maara > 0:
        n = 0  # Lasketaan montako pistettä osuu ympyrän sisään
        laskuri = 0

        while laskuri < pisteiden_maara:
            x = random.uniform(-1, 1)
            y = random.uniform(-1, 1)
            
            # Tarkistetaan onko piste (x, y) yksikköympyrän sisällä
            if x**2 + y**2 < 1:
                n += 1

            laskuri += 1

        # Lasketaan piin likiarvo
        pi_likiarvo = 4 * n / pisteiden_maara
        print(f"Piin likiarvo {pisteiden_maara} pisteellä on noin: {pi_likiarvo:.6f}")
    else:
        print("Pisteiden määrän täytyy olla positiivinen kokonaisluku.")
else:
    print("Syötteen täytyy olla positiivinen kokonaisluku.")
