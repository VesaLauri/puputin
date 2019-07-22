import unittest
import puputin as pt


class test_puputin(unittest.TestCase):
    def test_puptinluonti(self):
        tp = pt.puputin("testipuputin")
        self.assertEqual(tp.nimi, "testipuputin", "Nimi property ei toimi")
