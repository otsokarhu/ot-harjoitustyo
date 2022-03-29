import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti

class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.kassapaate = Kassapaate()

    def test_luotukasssa(self):
        self.assertNotEqual(self.kassapaate, None)

    def test_saldo_oikein(self):
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
    
    def test_lounaita_nolla(self):
        lounaat = self.kassapaate.edulliset + self.kassapaate.maukkaat
        self.assertEqual(lounaat, 0)

    def test_kateisosto_edullinen_saldoa(self):
        self.kassapaate.syo_edullisesti_kateisella(250)
        self.assertEqual(self.kassapaate.edulliset, 1)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100240)
        self.assertEqual(str(self.kassapaate.syo_edullisesti_kateisella(250)), "10")

    def test_kateisosto_edullinen_ei_saldoa(self):
        self.kassapaate.syo_edullisesti_kateisella(230)
        self.assertEqual(self.kassapaate.edulliset, 0)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        self.assertEqual(str(self.kassapaate.syo_edullisesti_kateisella(230)), "230")

    def test_kateisosto_maukas_saldoa(self):
        self.kassapaate.syo_maukkaasti_kateisella(450)
        self.assertEqual(self.kassapaate.maukkaat, 1)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100400)
        self.assertEqual(str(self.kassapaate.syo_maukkaasti_kateisella(450)), "50")

    def test_kateisosto_maukkaasti_ei_saldoa(self):
        self.kassapaate.syo_maukkaasti_kateisella(230)
        self.assertEqual(self.kassapaate.maukkaat, 0)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        self.assertEqual(str(self.kassapaate.syo_maukkaasti_kateisella(230)), "230")

    def test_kortti_edullinen_saldo(self):
        mkortti = Maksukortti(260)
        aktio = self.kassapaate.syo_edullisesti_kortilla(mkortti)
        self.assertEqual(str(mkortti), "saldo: 0.2")
        self.assertEqual(aktio, True)
        self.assertEqual(self.kassapaate.edulliset, 1)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_kortti_edullinen_ei_saldo(self):
        mkortti = Maksukortti(220)
        aktio = self.kassapaate.syo_edullisesti_kortilla(mkortti)
        self.assertEqual(str(mkortti), "saldo: 2.2")
        self.assertEqual(aktio, False)
        self.assertEqual(self.kassapaate.edulliset, 0)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_kortti_maukas_saldo(self):
        mkortti = Maksukortti(460)
        aktio = self.kassapaate.syo_maukkaasti_kortilla(mkortti)
        self.assertEqual(str(mkortti), "saldo: 0.6")
        self.assertEqual(aktio, True)
        self.assertEqual(self.kassapaate.maukkaat, 1)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_kortti_maukas_ei_saldo(self):
        mkortti = Maksukortti(220)
        aktio = self.kassapaate.syo_maukkaasti_kortilla(mkortti)
        self.assertEqual(str(mkortti), "saldo: 2.2")
        self.assertEqual(aktio, False)
        self.assertEqual(self.kassapaate.maukkaat, 0)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_kortti_lataus(self):
        mkortti = Maksukortti(10)
        alku = str(mkortti)
        self.kassapaate.lataa_rahaa_kortille(mkortti, 20)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100020)
        self.assertNotEqual(str(mkortti), alku)
        
    def test_kortti_lataus_ilman_rahaa(self):
        mkortti = Maksukortti(10)
        alku = str(mkortti)
        self.kassapaate.lataa_rahaa_kortille(mkortti, -10)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        self.assertEqual(str(mkortti), alku)

    

    


    