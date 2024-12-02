KAPASITEETTI = 5
OLETUSKASVATUS = 5

class IntJoukko:
    def _luo_lista(self, koko):
        return [0] * koko
    
    def __init__(self, kapasiteetti=None, kasvatuskoko=None):
        self.kapasiteetti = self._validoi_parametri(kapasiteetti, KAPASITEETTI, "Väärä kapasiteetti")
        self.kasvatuskoko = self._validoi_parametri(kasvatuskoko, OLETUSKASVATUS, "Väärä kasvatuskoko")
        self.luvut = self._luo_lista(self.kapasiteetti)
        self.lukumaara = 0

    def _validoi_parametri(self, arvo, oletus, virheviesti):
        if arvo is None:
            return oletus
        if not isinstance(arvo, int) or arvo < 0:
            raise Exception(virheviesti)
        return arvo

    def kuuluu(self, luku):
        return luku in self.luvut[:self.lukumaara]

    def lisaa(self, luku):
        if not self.kuuluu(luku):
            if self.lukumaara >= len(self.luvut):
                self._kasvata_taulukkoa()
            self.luvut[self.lukumaara] = luku
            self.lukumaara += 1
            return True
        return False

    def _kasvata_taulukkoa(self):
        vanha_luvut = self.luvut
        self.luvut = self._luo_lista(len(vanha_luvut) + self.kasvatuskoko)
        self._kopioi_lista(vanha_luvut, self.luvut)

    def poista(self, luku):
        if luku in self.luvut[:self.lukumaara]:
            self.luvut.remove(luku)
            self.lukumaara -= 1
            return True
        return False

    def _kopioi_lista(self, vanha, uusi):
        for i in range(len(vanha)):
            uusi[i] = vanha[i]

    def mahtavuus(self):
        return self.lukumaara

    def to_int_list(self):
        return self.luvut[:self.lukumaara]

    @staticmethod
    def yhdiste(a, b):
        tulos = IntJoukko()
        for numero in a.to_int_list() + b.to_int_list():
            tulos.lisaa(numero)
        return tulos

    @staticmethod
    def leikkaus(a, b):
        tulos = IntJoukko()
        for numero in a.to_int_list():
            if numero in b.to_int_list():
                tulos.lisaa(numero)
        return tulos

    @staticmethod
    def erotus(a, b):
        tulos = IntJoukko()
        for numero in a.to_int_list():
            tulos.lisaa(numero)
        for numero in b.to_int_list():
            tulos.poista(numero)
        return tulos

    def __str__(self):
        return "{" + ", ".join(map(str, self.luvut[:self.lukumaara])) + "}"
