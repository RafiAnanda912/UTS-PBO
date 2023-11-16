class Mobil:
    def __init__(self, merk, warna):
        self.merk = merk  # Variabel instance publik
        self.__warna = warna  # Variabel instance privat

    def info(self):
        return f"Mobil {self.merk}, warna {self.__warna}"

    def ganti_warna(self, warna_baru):
        self.__warna = warna_baru

# Membuat objek
mobil1 = Mobil("Toyota", "Merah")

# Mengakses variabel publik
print(mobil1.merk)  # Output: Toyota

# Mengakses variabel privat (tidak disarankan, seharusnya diakses melalui metode)
# print(mobil1.__warna)  # Ini akan menghasilkan kesalahan

# Mengakses variabel privat melalui metode
print(mobil1.info())  # Output: Mobil Toyota, warna Merah

# Mengubah warna melalui metode
mobil1.ganti_warna("Biru")
print(mobil1.info())  # Output: Mobil Toyota, warna Biru
