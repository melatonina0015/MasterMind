import unittest
from mastermind import Wyjatki

class TestTurnsEntry(unittest.TestCase):

    def test_malo_rund(self):
        klasa = Wyjatki()


        result = klasa.wyjatekSprawdzIloscRund(7)
        self.assertEqual(result,1)
        result = klasa.wyjatekSprawdzIloscRund(4)
        self.assertEqual(result,1)
        result = klasa.wyjatekSprawdzIloscRund(0)
        self.assertEqual(result,1)
        result = klasa.wyjatekSprawdzIloscRund(-2)
        self.assertEqual(result,1)

    def test_duzo_rund(self):
        klasa = Wyjatki()

        result = klasa.wyjatekSprawdzIloscRund(13)
        self.assertEqual(result,2)
        result = klasa.wyjatekSprawdzIloscRund(18)
        self.assertEqual(result,2)
        result = klasa.wyjatekSprawdzIloscRund(100000)
        self.assertEqual(result,2)

class TestKodGracza(unittest.TestCase):

    def test_za_mala_cyfra(self):
        klasa = Wyjatki()

        result = klasa.wyjatekSprawdzKod([0,1,3,4])
        self.assertEqual(result, 1)
        result = klasa.wyjatekSprawdzKod([4,0,3,4])
        self.assertEqual(result, 1)
        result = klasa.wyjatekSprawdzKod([3,1,0,4])
        self.assertEqual(result, 1)
        result = klasa.wyjatekSprawdzKod([5,1,3,0])
        self.assertEqual(result, 1)

    def test_za_duza_cyfra(self):
        klasa = Wyjatki()

        result = klasa.wyjatekSprawdzKod([11,1,3,4])
        self.assertEqual(result, 2)
        result = klasa.wyjatekSprawdzKod([4,18,3,4])
        self.assertEqual(result, 2)
        result = klasa.wyjatekSprawdzKod([3,2,7,4])
        self.assertEqual(result, 2)
        result = klasa.wyjatekSprawdzKod([5,1,3,10])
        self.assertEqual(result, 2)


if __name__ == '__main__':
    unittest.main()
    print("Testy udane!")
