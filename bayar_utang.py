import submodules
from pilih_dompet import pilih_dompet, tulis_dompet
from pemasukan_pengeluaran import rekap_pemasukan_pengeluaran

def bayar_utang(nama:str, dompet:int, nominal:int):
    rekap_pemasukan_pengeluaran("1", "utang", dompet, nominal)

    toadd = [[ nama, nominal ]]

    submodules.open_append_csv("utang.csv", toadd)

if __name__ == "__main__":
    bayar_utang("Utang Rakha","umum", 12000)