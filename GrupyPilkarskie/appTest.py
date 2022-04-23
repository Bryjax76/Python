import app
import unittest
import os

class Testowanie(unittest.TestCase):

    def test_dlugoscA(self):
        dlugoscA = len(app.grupaA)
        self.assertEqual((dlugoscA),(4))

    def test_dlugoscB(self):
        dlugoscB = len(app.grupaB)
        self.assertEqual((dlugoscB),(4))

    def test_dlugoscC(self):
        dlugoscC = len(app.grupaC)
        self.assertEqual((dlugoscC),(4))

    def test_dlugoscD(self):
        dlugoscD = len(app.grupaD)
        self.assertEqual((dlugoscD),(4))

    def test_zespoly(self):
        dlugoscall = len(app.x)
        self.assertEqual((dlugoscall),(16))

    def test_powtarzalnosc_panstwa(self):
        powtarzalnosc = app.sum.count("Polska")
        self.assertEqual((powtarzalnosc),(0))

    def test_polska_niemcy(self):
        Lista = app.grupaA
        ListaB = app.grupaB
        ListaC = app.grupaC
        ListaD = app.grupaD
        if 'Polska' in Lista:
            if 'Niemcy' in Lista:
                result = False
            else:
                result = True
        else:
            if 'Polska' in ListaB:
                if 'Niemcy' in ListaB:
                    result = False
                else:
                    result = True
            else:
                if 'Polska' in ListaC:
                    if 'Niemcy' in ListaC:
                        result = False
                    else:
                        result = True
                else: 
                    if 'Polska' in ListaD:
                        if 'Niemcy' in ListaD:
                            result = False
                        else:
                            result = True
        self.assertEqual((result),(True))


if __name__ == '__main__':
    unittest.main()