def bagi(a, b):
    try:
        hasil = a / b
        return hasil
    except ZeroDivisionError:
        print("Error: Pembagian oleh nol tidak diizinkan.")
        return None
    except TypeError as e:
        print(f"Error: {e}")
        return None
    except Exception as e:
        print(f"Error umum: {e}")
        return None

# Contoh pemanggilan fungsi dengan penanganan exception
angka1 = 10
angka2 = 0

hasil_pembagian = bagi(angka1, angka2)

if hasil_pembagian is not None:
    print(f"Hasil pembagian {angka1} / {angka2} adalah {hasil_pembagian}")
else:
    print("Gagal melakukan pembagian.")
