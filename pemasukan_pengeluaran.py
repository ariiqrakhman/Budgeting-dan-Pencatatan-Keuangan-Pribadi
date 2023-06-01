import submodules
from pilih_dompet import pilih_dompet, tulis_dompet
from datetime import date

def rekap_pemasukan_pengeluaran(kode:str, tipe:str, dompet:str, nominal:int):
    tanggal = (date.today()).strftime("%Y/%m/%d")

    toadd = [[ tanggal, kode, tipe, dompet, nominal ]]

    submodules.open_append_csv("sejarah_transaksi.csv", toadd)

    tulis_dompet(dompet, kode, nominal)

# def pemasukan_pengeluaran():

if __name__ == "__main__":
    rekap_pemasukan_pengeluaran("0", "dll", "umum", 40000)
