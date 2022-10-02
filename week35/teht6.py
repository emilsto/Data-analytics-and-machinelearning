class Murtoluku:
    def __init__(self, osoittaja, nimittaja):
        self.osoittaja = osoittaja
        self.nimittaja = nimittaja
    def tulosta(self):
        print (f'{self.osoittaja}/{self.nimittaja}')
    def sievenna(self):
        s = self.syt()
        osoittaja = self.osoittaja / s
        self.osoittaja = int(osoittaja)
        
        nimittaja = self.nimittaja / s
        self.nimittaja = int(nimittaja)
        
        
    def syt(self):
        a = self.osoittaja
        b = self.nimittaja
        while b != 0:
            t = b
            b = a % b
            a = t
        return a
        
        
        
ml = Murtoluku(34562, 311058)

ml.tulosta()
ml.sievenna()
ml.tulosta()