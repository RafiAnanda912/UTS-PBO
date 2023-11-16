import tkinter as tk

def tombol_ditekan():
    label_var.set("Tombol Ditekan!")

# Membuat jendela utama
jendela_utama = tk.Tk()
jendela_utama.title("Contoh GUI")

# Membuat tombol dan menambahkannya ke jendela
tombol = tk.Button(jendela_utama, text="Tekan Saya", command=tombol_ditekan)
tombol.pack(pady=20)

# Membuat label untuk menampilkan pesan
label_var = tk.StringVar()
label_var.set("Selamat Datang!")

label = tk.Label(jendela_utama, textvariable=label_var)
label.pack()

# Memulai loop utama GUI
jendela_utama.mainloop()
