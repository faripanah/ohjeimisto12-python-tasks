from hissi import Hissi
class Talo :
    def __init__(self, alin, ylin,maara):
        self.alin_kerros = alin
        self.ylin_kerros = ylin
        self.hissi_lukumaraa = maara
        self.hissit = []
        for i in range(maara):
            self.hissit.append(Hissi(self.alin_kerros, self.ylin_kerros))




    def aja_hissiä(self, hissi_numero, kohdekerros):
        if hissi_numero >self.hissi_lukumaraa or hissi_numero < 1:
            print('hissiä ei ole!!!!')
        else:
            self.hissit[hissi_numero-1].siirry_kerrokseen(kohdekerros)



    def palohälytys(self):
        for hissi in self.hissit:
            hissi.siirry_kerrokseen(self.alin_kerros)

