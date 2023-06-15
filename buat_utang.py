import submodules as sdl
from pilih_dompet import pilih_dompet
from pemasukan_pengeluaran import rekap_pemasukan_pengeluaran

def rekap_utang(nama:str, dompet:int, nominal:int):
    # Akses tanggal pembuatan transaksi (hari ini)
    rekap_pemasukan_pengeluaran(1, "utang", dompet, nominal)

    # Persiapan list ditulis ke csv
    toadd = [[ nama, nominal ]]

    # Penulisan ke csv pada index value pertama
    sdl.open_append_csv("utang.csv", toadd)
    
def buat_utang():
    while True: # Pengulangan selama belum keluar dari subprogram
        # Identitas Subprogram
        print("\n"+"BUAT UTANG".center(50,"=")+"\n")    

        # pilih dompet untuk mencatat utang
        dompet, nominal_dompet = pilih_dompet()
        
        # meminta pengguna memasukkan nama utang
        nama_utang = sdl.input_normal("Masukkan nama utang: ")

        # meminta pengguna memasukkan nominal utang
        nominal_utang = sdl.input_money("Masukkan nominal utang: ")

        # Konfirmasi buat utang
        dis_nom = f"Rp{nominal_utang:,}"
        print(f'''Konfirmasi pembuatan transaksi:
Transaksi {sdl.ch_color_style("pemasukan","sky")}
Tipe {sdl.ch_color_style("utang","sky")}
Nominal {sdl.ch_color_style(dis_nom,"sky")} pada dompet {sdl.ch_color_style(dompet,"sky")}
''')
        
        # memberikan pilihan kepada pengguna apakah ingin menyelesaikan pembuatan utang atau tidak
        finalisasi = sdl.input_of_yatidak("Apakah Anda ingin finalisasi pembuatan utang? (y/t) ")
        
        # jika pengguna ingin menyelesaikan pembuatan utang
        if finalisasi == "y":
            # menambahkan data utang ke file CSV
            rekap_utang(nama_utang, dompet, nominal_utang)
            # keluar dari loop while
            break
        
        # jika pengguna tidak ingin menyelesaikan pembuatan utang    
        elif finalisasi == "t":
            # meminta pengguna memilih apakah ingin membuat utang baru atau tidak
            buat_lagi = sdl.input_of_yatidak("Apakah Anda ingin membuat utang baru? (input t untuk keluar dari subprogram) (y/t): ")
            # jika pengguna tidak ingin membuat utang baru
            if buat_lagi == "t":
                # keluar dari loop while
                break

if __name__ == "__main__":
    buat_utang()
