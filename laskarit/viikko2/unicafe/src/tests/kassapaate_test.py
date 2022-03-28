import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti

class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.kassa = Kassapaate()
        self.kortti = Maksukortti(1000)

    def test_kateis_osto_edullinen(self):
        self.assertEqual(self.kassa.syo_edullisesti_kateisella(240), 0)
        self.assertEqual(self.kassa.edulliset, 1)
        self.assertEqual(self.kassa.kassassa_rahaa, 100240)

    def test_kateis_osto_edullinen_ei_toimi(self):
        self.assertEqual(self.kassa.kassassa_rahaa, 100000)
        self.assertEqual(self.kassa.syo_edullisesti_kateisella(100), 100)
        
    def test_kateis_osto_maukas(self):
        self.assertEqual(self.kassa.syo_maukkaasti_kateisella(400), 0)
        self.assertEqual(self.kassa.maukkaat, 1)
        self.assertEqual(self.kassa.kassassa_rahaa, 100400)

    def test_kateis_osto_maukas_ei_toimi(self):
        self.assertEqual(self.kassa.kassassa_rahaa, 100000)
        self.assertEqual(self.kassa.syo_maukkaasti_kateisella(300), 300)

    def test_kortti_osto_edullinen(self):
        self.assertEqual(self.kassa.syo_edullisesti_kortilla(self.kortti), True)
        self.assertEqual(self.kassa.edulliset, 1)

    def test_kortti_osto_maukas(self):
        self.assertEqual(self.kassa.syo_maukkaasti_kortilla(self.kortti), True)
        self.assertEqual(self.kassa.maukkaat, 1)
    
    def test_kortti_osto_edullinen_ei_toimi(self):
        self.kortti.ota_rahaa(240)
        self.kortti.ota_rahaa(240)
        self.kortti.ota_rahaa(240)
        self.kortti.ota_rahaa(240)
        self.assertEqual(self.kassa.syo_edullisesti_kortilla(self.kortti), False)

    def test_kortti_osto_maukas_ei_toimi(self):
        self.kortti.ota_rahaa(400)
        self.kortti.ota_rahaa(400)
        self.assertEqual(self.kassa.syo_maukkaasti_kortilla(self.kortti), False)

    def test_korttiosto_ei_vaikuta_kassaan(self):
        self.assertEqual(self.kassa.syo_maukkaasti_kortilla(self.kortti), True)
        self.assertEqual(self.kassa.kassassa_rahaa, 100000)

    def test_lataa_rahaa_kortille(self):
        self.kassa.lataa_rahaa_kortille(self.kortti, 1000)
        self.assertEqual(self.kassa.kassassa_rahaa, 101000)

    def test_lataus_kortille_ei_toimi(self):
        self.kassa.lataa_rahaa_kortille(self.kortti, -1000)
        self.assertEqual(self.kassa.kassassa_rahaa, 100000)
        self.assertEqual(self.kassa.lataa_rahaa_kortille(self.kortti, -1000), None)


    