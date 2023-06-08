import submodules
from pilih_dompet import pilih_dompet, tulis_dompet
from pemasukan_pengeluaran import rekap_pemasukan_pengeluaran

def bayar_utang():
    # Membuka file CSV dan mendapatkan header dan daftar utang
    header, list_utang = submodules.open_read_csv("utang.csv")

    # Memeriksa apakah ada utang dalam daftar
    if len(list_utang) >= 1:
        # Menampilkan daftar utang
        for ele in list_utang:
            print(ele[0], ele[1])
        print("keluar")

        # Menyiapkan opsi pembayaran utang, termasuk opsi "keluar"
        opsi = [ele[0] for ele in list_utang]


        # Meminta pengguna untuk memilih utang yang akan dibayar atau keluar dari program
        while True:    
            utang_bayar = submodules.input_of_options('Masukkan nama utang atau ketik "keluar" untuk keluar', opsi + ["keluar"])
            if utang_bayar == "keluar":
                print("Konfirmasi keluar")
                return None
            elif utang_bayar in opsi:
                ind_utang = opsi.index(utang_bayar)
                nominal_utang = int(list_utang[ind_utang][1])
        
            # Melanjutkan ke langkah selanjutnya: memilih dompet dan nominal pembayaran
            dompet, nominaldompet = pilih_dompet()

            # Input nominal bayar utang
            while True:
                try:
                    dibayar = submodules.input_money_w_params("Masukkan nominal bayar utang? ","0", nominaldompet)
                    assert nominal_utang - dibayar >= 0, f"Nominal bayar terlalu banyak, maksimal {nominal_utang}"
                    break
                except AssertionError as er:
                    print(er)
        
            # Konfirmasi bayar utang
            print(f'''Konfirmasi:
nama utang = {utang_bayar}
nominal utang = {nominal_utang}
dibayar = {dibayar}''')
            
            konfir_bayar = submodules.input_of_yatidak("Apakah mau membayar utang? (y/t) ")
            if konfir_bayar == "y":
                break
        
        # Pengurangan utang
        list_utang[ind_utang][1] = nominal_utang - dibayar
        if list_utang[ind_utang][1] == 0:
            list_utang.pop(ind_utang)
        
        # Penulisan file utang
        submodules.open_write_all_csv("utang.csv", list_utang, header)

        # Penulisan rekap pemasukan/pengeluaran
        rekap_pemasukan_pengeluaran("0", "bayar utang", dompet, dibayar)
        
    # Apabila tidak ada utang
    else:
        print('Tidak ada utang')


if __name__ == "__main__":
    bayar_utang()