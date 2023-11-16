import sqlite3

def buat_tabel():
    conn = sqlite3.connect("kontak.db")
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS kontak (id INTEGER PRIMARY KEY, nama TEXT, nomor TEXT)")
    conn.commit()
    conn.close()

def tambah_kontak(nama, nomor):
    conn = sqlite3.connect("kontak.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO kontak (nama, nomor) VALUES (?, ?)", (nama, nomor))
    conn.commit()
    conn.close()
    print("Kontak berhasil ditambahkan!")

def lihat_kontak():
    conn = sqlite3.connect("kontak.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM kontak")
    kontak = cursor.fetchall()
    conn.close()

    if not kontak:
        print("Daftar kontak kosong.")
    else:
        print("Daftar Kontak:")
        for row in kontak:
            print(f"ID: {row[0]}, Nama: {row[1]}, Nomor: {row[2]}")

if __name__ == "__main__":
    buat_tabel()

    while True:
        print("\nMenu:")
        print("1. Tambah Kontak")
        print("2. Lihat Kontak")
        print("3. Keluar")

        pilihan = input("Pilih menu (1/2/3): ")

        if pilihan == "1":
            nama = input("Masukkan nama kontak: ")
            nomor = input("Masukkan nomor kontak: ")
            tambah_kontak(nama, nomor)
        elif pilihan == "2":
            lihat_kontak()
        elif pilihan == "3":
            print("Program selesai.")
            break
        else:
            print("Pilihan tidak valid. Silakan pilih lagi.")
