class Bentuk:
    def hitung_luas(self):
        print("Luas bentuk umum")


class Segitiga(Bentuk):
    def hitung_luas(self):
        print("Luas segitiga")


class Lingkaran(Bentuk):
    def hitung_luas(self):
        print("Luas lingkaran")


# Fungsi yang menerima objek Bentuk dan memanggil metode hitung_luas
def proses_bentuk(bentuk):
    bentuk.hitung_luas()


# Objek dari kelas turunan
segitiga = Segitiga()
lingkaran = Lingkaran()

# Memanggil fungsi dengan objek kelas turunan
proses_bentuk(segitiga)  # Output: Luas segitiga
proses_bentuk(lingkaran)  # Output: Luas lingkaran
