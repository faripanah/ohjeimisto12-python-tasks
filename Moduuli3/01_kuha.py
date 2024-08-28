pituus_alle= 37
kuha_pituus = float(input("Anna kuhan pituuden senttimetreinä: "))
if kuha_pituus < pituus_alle :
    puuttuu = pituus_alle - kuha_pituus
    print(f"Kuha on alemittainen. Laske kuha takaisin järveen. {puuttuu:.1f} cm on lyhyt.")
else:
    print("Voit pitää kuhan.")
