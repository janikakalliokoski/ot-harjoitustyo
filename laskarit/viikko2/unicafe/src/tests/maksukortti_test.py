import unittest
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.maksukortti = Maksukortti(10)

    def test_luotu_kortti_on_olemassa(self):
        self.assertNotEqual(self.maksukortti, None)

    def test_saldo_alussa_oikein(self):
        self.assertEqual(str(self.maksukortti), "saldo: 0.1")

    def test_lataus_oikein(self):
        self.maksukortti.lataa_rahaa(25)
        self.assertEqual(str(self.maksukortti), "saldo: 0.35")

    def test_rahan_ottaminen_toimii_rahaa_on_riittävästi(self):
        self.maksukortti.ota_rahaa(4)
        self.assertEqual(str(self.maksukortti), "saldo: 0.06")
        return True

    def test_rahan_ottaminen_toimii_rahaa_ei_riittävästi(self):
        self.maksukortti.ota_rahaa(11)
        self.assertEqual(str(self.maksukortti), "saldo: 0.1")
        return False