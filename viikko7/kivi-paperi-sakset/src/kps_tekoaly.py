from tekoaly import Tekoaly
from kivi_paperi_sakset import KiviPaperiSakset

class KPSTekoaly(KiviPaperiSakset):
    def __init__(self):
        self.tekoaly = Tekoaly()

    def _toisen_siirto(self, ensimmaisen_siirto):
        return self.tekoaly.anna_siirto()
