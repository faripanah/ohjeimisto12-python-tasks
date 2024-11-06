class Hissi:
    def __init__(self, alin, ylin) :
        self.alin_kerros = alin
        self.ylin_kerros = ylin
        self.nykyinen_kerros = alin

    def siirry_kerrokseen(self, kohdekerros):
        if kohdekerros < self.alin_kerros or kohdekerros > self.ylin_kerros:
            print('kerrosta ei ole olemassa!!')
        while kohdekerros < self.nykyinen_kerros:
            self.kerros_alas()
            

        while kohdekerros > self.nykyinen_kerros:
            self.kerros_ylös()
            
        
     
    def kerros_ylös(self):
        self.nykyinen_kerros += 1
        print(f'Nykyinen kerros on : {self.nykyinen_kerros}')

    def kerros_alas(self):
        self.nykyinen_kerros -= 1
        print(f'Nykyinen kerros on : {self.nykyinen_kerros}')
