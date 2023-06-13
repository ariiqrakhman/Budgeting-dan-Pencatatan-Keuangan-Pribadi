from datetime import date
from pemasukan_pengeluaran import pemasukan_pengeluaran
from transfer_akun import transfer_akun
from buat_utang import buat_utang
from bayar_utang import bayar_utang
from edit_tipe import edit_tipe
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
        print()
        print(" SELAMAT DATANG DI PROGRAM ".center(50,"="))
        print(" BUDGETING DAN PENCATATAN ".center(50,"="))
        print(" KEUANGAN PRIBADI ".center(50,"="))
        print()

        # Tampilkan dompet dan utang
        menampilkan_dompet_utang()
        print()

        # Opsi menu
        menu = [
            [1, "Pemasukan / Pengeluaran", pemasukan_pengeluaran],
            [2, "Transfer Akun", transfer_akun],
            [3, "Buat Utang", buat_utang],
            [4, "Bayar Utang", bayar_utang],
            [5, "Edit Tipe", edit_tipe],
            [6, "Analisis Keuangan", analisis_keuangan],
            [7, "Invoice", invoice],
            [0, "Keluar", None]
        ]
        opsi = list(range(8))

        # Tampilkan menu
        submodules.display_table([ [ ele[0], ele[1] ] for ele in menu ], ["", "Menu"])
        print()
        pilih_menu = submodules.input_of_int_options("Input 1-7 untuk pilih menu atau 0 untuk keluar ", opsi)

        if pilih_menu != 0:
            system("cls")
            menu[pilih_menu-1][2]()
            _ = submodules.input_normal(submodules.ch_color_style("Tekan Enter untuk kembali ke menu utama", "yellow"))
            print("... Proses")
            sleep(.75)
            print("... Kembali ke")
            sleep(.75)
            print("... Menu utama")
            sleep(.75)
            print("... --------")
            sleep(.75)

        else:
            konfir_keluar = submodules.input_of_yatidak("Anda yakin mau keluar? (y/t)")
            if konfir_keluar == "y":
                print(submodules.ch_color_style("JUMPA LAGI, SEMANGAT BERHEMAT","orange"))
                break

if __name__ == "__main__":
    main()