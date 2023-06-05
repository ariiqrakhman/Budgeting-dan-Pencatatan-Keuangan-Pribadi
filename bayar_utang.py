import submodules
from pilih_dompet import pilih_dompet, tulis_dompet
from pemasukan_pengeluaran import rekap_pemasukan_pengeluaran

def bayar_utang(nama:str, dompet:int, nominal:int):
    # Membuka file CSV dan mendapatkan header dan daftar utang
    header, list_utang = submodules.open_read_csv("utang.csv")

    # Memeriksa apakah ada utang dalam daftar
    if len(list_utang) >= 1:
        # Menampilkan daftar utang
        for ele in list_utang:
            print(ele[0], ele[1])

        # Menyiapkan opsi pembayaran utang, termasuk opsi "keluar"
        opsi = [ele[0] for ele in list_utang] + ["keluar"]

        # Meminta pengguna untuk memilih utang yang akan dibayar atau keluar dari program
        while True:
            utang_bayar = submodules.input_of_options(prompt='Masukkan nama utang atau ketik "keluar" untuk keluar', opsi)
            if utang_bayar == "keluar":
                print("Konfirmasi keluar")
                return

            # Melanjutkan ke langkah selanjutnya: memilih dompet dan nominal pembayaran
            dompet, nominal = pilih_dompet()

    else:
        print('Tidak ada utang')


if __name__ == "__main__":
    bayar_utang("Utang Rakha","umum", 12000)