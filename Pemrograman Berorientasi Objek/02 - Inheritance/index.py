class pustakawanPerpustakaan:
    def __init__(self, id, nama):
        self.id = id
        self.nama = nama
        self.buku = []
    
    def tambahkanBuku(self, newBook):
        self.buku.append(newBook)
        print("Buku ({}) berhasil di tambahkan.\nOleh: {}, ({})".format(
            newBook,
            self.nama,
            self.id
        ))

    def lihatBuku(self):
        for no, i in enumerate(self.buku, start=0):
            print("{}. {}".format(
                no,
                i
            ))

    def hapusBuku(self, userInput):
        if 0 <= userInput < len(self.buku):
            del self.buku[userInput]
            print("Berhasil menghapus buku")
        else:
            print("Buku tidak ada")

# Pewarisan kelas
class anggotaPerpustakaan(pustakawanPerpustakaan):
    def __init__(self, id, nama):
        # Pewarisan atribut
        super().__init__(id, nama)

    # Pewarisan method
    def informasiAnggota(self):
        print("Id: {}, Nama: {}".format(
            self.id,
            self.nama
        ))
    
    # Pewarisan method
    def meminjamBuku(self, buku):
        print("Buku ({}) berhasil di pinjam!".format(
            buku
        ))

    # Pewarisan method
    def mengembalikanBuku(self, buku):
        print("Buku ({}) berhasil di dikembalikan!".format(
            buku
        ))

# Bukan variabel, tapi Objek
pustakawan = pustakawanPerpustakaan("101", "Titozaki")
pustakawan.tambahkanBuku("Mein Kampf")
pustakawan.lihatBuku()
pustakawan.hapusBuku(0)

anggota = anggotaPerpustakaan("101", "Yogawan")
anggota.informasiAnggota()
anggota.meminjamBuku("Mein Kampf")
anggota.mengembalikanBuku("Mein Kampf")