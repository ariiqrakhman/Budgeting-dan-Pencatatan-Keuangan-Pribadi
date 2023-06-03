import submodules
from pilih_dompet import pilih_dompet, tulis_dompet
from pemasukan_pengeluaran import rekap_pemasukan_pengeluaran

def rekap_utang(nama:str, dompet:int, nominal:int):
    rekap_pemasukan_pengeluaran("1", "utang", dompet, nominal)

    toadd = [[ nama, nominal ]]

    submodules.open_append_csv("utang.csv", toadd)

# def buat_utang():

if __name__ == "__main__":
    rekap_utang("utang Dea", "umum", 100000)
    
def buat_utang():
    while True:
        dompet = input_of_options("Pilih dompet (A/B): ", ["a", "b"])
        nama_utang = input_normal("Masukkan nama utang: ")
        nominal_utang = input_money("Masukkan nominal utang: ")
        finalisasi = input_of_yatidak("Apakah Anda ingin finalisasi pembuatan utang? (y/t): ")
        
        if finalisasi == "y":
            header, content = open_read_csv("rekap_utang.csv")
            content.append([dompet, nama_utang, nominal_utang])
            open_write_all_csv("rekap_utang.csv", content, header)
            print("Utang berhasil dibuat!")
            break
        elif finalisasi == "t":
            buat_lagi = input_of_yatidak("Apakah Anda ingin membuat utang baru? (y/t): ")
            if buat_lagi == "t":
                print("Selesai")
                break
            elif buat_lagi == "y":
                continue
