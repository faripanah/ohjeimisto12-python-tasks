LUOTI_GR = 13.3
NAULAT_GR = 32*LUOTI_GR
LEIVISKA_GR = 20*NAULAT_GR

leiviskät = float(input("Anna leiviskät:"))
naulat = float(input("Anna naulat:"))
luodit = float(input("Anna luodit:"))
grammat_leiviskät = leiviskät * LEIVISKA_GR
grammat_naulat = naulat * NAULAT_GR
grammat_luodit = luodit * LUOTI_GR

kaikkigrammat = grammat_leiviskät + grammat_naulat + grammat_luodit
kilo = int(kaikkigrammat // 1000)
loputgrammat = kaikkigrammat % 1000
print("Massa nykymittojen mukaan:")
print(f"{kilo} kilogrammaa ja {loputgrammat:.2f} grammaa.")
