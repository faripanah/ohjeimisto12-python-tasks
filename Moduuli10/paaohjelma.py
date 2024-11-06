from hissi import Hissi
from talo import Talo
hissi1 = Hissi(1,10)
hissi2 = Hissi(2,8)
hissi1.siirry_kerrokseen(5)
hissi1.siirry_kerrokseen(3)



talo1 = Talo(1,10,4)
talo1.aja_hissiä(2, 5)

print("Palohälytys!!! kaikki hissit pojakerrokseen.")
talo1.palohälytys()
