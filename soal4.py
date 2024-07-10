class Buah:
    def __init__(self, nama, warna, rasa):
        self.nama = nama
        self.warna = warna
        self.rasa = rasa
    def set_nama(self, nama):
        self.nama = nama
    def set_warna(self, warna):
        self.warna = warna
    def set_rasa(self, rasa):
        self.rasa = rasa
    def informasi_buah(self):
        print(f'Nama Buah: ', self.nama)
        print(f'Warna Buah: ', self.warna)
        print(f'Rasa Buah:', self.rasa)
class Mangga(Buah):
    def __init__(self, nama, warna, rasa, vitamin):
        super().__init__(nama, warna, rasa)
        self.__vitamin = vitamin

    def set_vitamin(self, vitamin):
        self.__vitamin = vitamin

    def informasi_Mangga(self):
        super().informasi_buah()
        print(f"Vitamin: {self.__vitamin}")