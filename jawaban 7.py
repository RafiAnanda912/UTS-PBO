import os
import tkinter as tk
from tkinter import filedialog, messagebox

class FileExplorerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("File Explorer App")

        self.current_directory = tk.StringVar()

        # Label untuk menunjukkan direktori saat ini
        label_director = tk.Label(root, textvariable=self.current_directory, font=("Helvetica", 12))
        label_director.pack(pady=10)

        # Listbox untuk menampilkan daftar file
        self.file_listbox = tk.Listbox(root, selectmode=tk.SINGLE)
        self.file_listbox.pack(expand=tk.YES, fill=tk.BOTH)

        # Tombol untuk membuka direktori
        button_open = tk.Button(root, text="Open Directory", command=self.buka_direktori)
        button_open.pack(pady=10)

        # Membuat listbox dan mengisi dengan daftar file
        self.perbarui_daftar_file()

    def buka_direktori(self):
        # Meminta pengguna untuk memilih direktori
        selected_directory = filedialog.askdirectory()

        if selected_directory:
            self.current_directory.set(f"Current Directory: {selected_directory}")
            os.chdir(selected_directory)
            self.perbarui_daftar_file()

    def perbarui_daftar_file(self):
        # Menghapus semua item dari listbox
        self.file_listbox.delete(0, tk.END)

        try:
            # Mendapatkan daftar file dalam direktori saat ini
            files = os.listdir()

            # Menambahkan setiap file ke dalam listbox
            for file in files:
                self.file_listbox.insert(tk.END, file)

        except Exception as e:
            messagebox.showerror("Error", f"Error: {e}")

if __name__ == "__main__":
    root = tk.Tk()
    app = FileExplorerApp(root)
    root.mainloop()
