import submodules
from pilih_dompet import pilih_dompet, tulis_dompet
from pemasukan_pengeluaran import rekap_pemasukan_pengeluaran

def rekap_utang(nama:str, dompet:int, nominal:int):
    rekap_pemasukan_pengeluaran("1", "utang", dompet, nominal)

    toadd = [[ nama, nominal ]]

    submodules.open_append_csv("utang.csv", toadd)

if __name__ == "__main__":
    <<<<<<< HEAD
    rekap_utang("utang Dea", "umum", 100000)
    
def buat_utang():
    while True:
        # pilih dompet untuk mencatat utang
        dompet, nominal_dompet = pilih_dompet()
        
        # meminta pengguna memasukkan nama utang
        nama_utang = submodules.input_normal("Masukkan nama utang: ")
        # meminta pengguna memasukkan nominal utang
        nominal_utang = submodules.input_money("Masukkan nominal utang: ")
        # memberikan pilihan kepada pengguna apakah ingin menyelesaikan pembuatan utang atau tidak
        finalisasi = submodules.input_of_yatidak("Apakah Anda ingin finalisasi pembuatan utang? (y/t): ")
        
        # jika penggunana ingin menyelesaikan pembuatan utang
        if finalisasi == "y":
            # menambahkan data utang ke file CSV
            rekap_utang(nama_utang, dompet, nominal_dompet)
            # keluar dari loop while
            break
        
        # jika pengguna tidak ingin menyelesaikan pembuatan utang    
        elif finalisasi == "t":
            
            # jika pengguna tidak ingin membuat utang baru
            # meminta pengguna memilih apakah ingin membuat utang baru atau tidak
            buat_lagi = submodules.input_of_yatidak("Apakah Anda ingin membuat utang baru? (y/t): ")
            if buat_lagi == "t":
                # keluar dari loop while
                break
            
=======
    rekap_utang("utang Dea", "umum", 100000)
>>>>>>> a0d406bd427a2aeaf863bce99f47c43298058096
