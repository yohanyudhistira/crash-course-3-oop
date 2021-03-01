from geometry.bangun_ruang import BangunRuang


class Segitiga(BangunRuang):
    def __init__(self, alas, tinggi):
        # Fungsi yang dipanggil pertama kali saat object diciptakan
        self.alas = alas
        self.tinggi = tinggi

    def info(self):
        return f'Ini adalah object dari Segitiga dengan alas = {self.alas} dan tinggi = {self.tinggi}'

    def hitung_luas(self):
        return self.alas * self.tinggi / 2

