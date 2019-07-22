import unittest
import puputin as pt


class test_puputin(unittest.TestCase):
    def test_puptinluonti(self):
        tp = pt.Puputin("testipuputin")
        self.assertEqual(tp.nimi, "testipuputin", "Nimi property ei toimi")

    def test_lisaapuppu(self):
        self.assertEqual(1, 1, "Nimi property ei toimi")

