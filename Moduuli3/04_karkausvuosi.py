vuosi_luku = int(input("Anna vuosiluku: "))
if (vuosi_luku % 4 == 0 and vuosi_luku % 100 != 0) or (vuosi_luku% 400 == 0):
    print(f"{vuosi_luku} on karkausvuosi")

else:
    print(f"{vuosi_luku} ei ole karkausvuosi.")

