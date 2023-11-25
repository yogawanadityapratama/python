class Nasabah:
    def __init__(self, id, nama, saldo):
        self.id = id
        self.nama = nama
        self.saldo = saldo
    
data_nasabah = []

def createNasabah():
    id = input("Masukan id nasabah: ")
    nama = input("Masukan nama nasabah: ")
    saldo = int(input("Masukan saldo nasabah: "))

    nasabah = Nasabah(id, nama, saldo)

    data_nasabah.append(nasabah)

def readNasabah():
    for i in data_nasabah:
        print("Id Nasabah: {}, Nama Nasabah: {}, Saldo: {}".format(
            i.id,
            i.nama,
            i.saldo
        ))

while True:
    print("Tama Fuckin Banking")
    print("1. Create Nasabah\n2. Read Nasabah")

    user_input = input("Pilih menu: ")

    match user_input:
        case "1":
            createNasabah()
        case "2":
            readNasabah()