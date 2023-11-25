class Mahasiswa:
    def __init__(self, nim, nama, alamat):
        self.nim = nim # Public
        self._nama = nama # Protected
        self.__alamat = alamat # Private