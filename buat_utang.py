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