from datetime import date
from pemasukan_pengeluaran import pemasukan_pengeluaran
from buat_utang import buat_utang
from bayar_utang import bayar_utang
from analisis_keuangan import analisis_keuangan
from invoice import invoice
from menampilkan_dompet_utang import menampilkan_dompet_utang
import submodules
from os import system
from time import sleep

def main():
    while True:
        # Bersihkan layar
        system("cls")

        # Tampilkan identitas program

        # Tampilkan dompet dan utang
        menampilkan_dompet_utang()

        # Opsi menu
        menu = [[1, pemasukan_pengeluaran],
                [2, buat_utang],
                [3, bayar_utang],
                [4, analisis_keuangan],
                [5, invoice],
                [0, "keluar"],
                ]
        dis = [[1, "pemasukan_pengeluaran"],
                [2, "buat_utang"],
                [3, "bayar_utang"],
                [4, "analisis_keuangan"],
                [5, "invoice"],
                [0, "keluar"],
                ]
        opsi = list(range(6))

        # Tampilkan menu
        submodules.display_table(dis, ["", "Menu"])
        pilih_menu = submodules.input_of_int_options("Input 1-5 untuk pilih menu atau 0 untuk keluar ", opsi)

        if pilih_menu != 0:
            menu[pilih_menu-1][1]()
            print("...")
            sleep(3)
            go = submodules.input_normal(submodules.ch_color_style("Tekan Enter untuk kembali ke menu utama", "yellow"))

        else:
            konfir_keluar = submodules.input_of_yatidak("Anda yakin mau keluar? (y/t)")
            if konfir_keluar == "y":
                break

if __name__ == "__main__":
    main()