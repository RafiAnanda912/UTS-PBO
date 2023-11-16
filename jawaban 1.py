# Kelas Induk atau Parent
class Hewan:
    def __init__(self, nama):
        self.nama = nama

    def bersuara(self):
        print("Bunyi hewan")

# Kelas Turunan atau Anak
class Anjing(Hewan):
    def bersuara(self):
        print("Guk guk")

# Kelas Turunan atau Anak
class Kucing(Hewan):
    def bersuara(self):
        print("Meong")

# Membuat objek dari kelas anak
dog = Anjing("Doggy")
cat = Kucing("Kitty")

# Memanggil metode dari kelas induk
dog.bersuara()  # Output: Guk guk

# Memanggil metode dari kelas induk
cat.bersuara()  # Output: Meong
