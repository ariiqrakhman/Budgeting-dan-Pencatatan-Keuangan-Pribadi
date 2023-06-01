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
pilih = pilih_dompet()
print(pilih)
inputpp = submodules.input_normal("0/1?")
if inputpp == 0 :
    submodules.input_money("Masukkan nominal pengeluaran :")
elif inputpp == 1 :
    submodules.input_money("Masukkan nominal pemasukan :")
else :
    pilih_dompet()

final = submodules.input_of_yatidak("Finalisasi pembuatan transaksi ?(y/t)")
print(final)
if final == "y" :
    toadd = [[ tanggal, kode, tipe, dompet, nominal ]]
    submodules.open_append_csv("sejarah_transaksi.csv", toadd)
elif final == "t" :
    transbaru = submodules.input_of_yatidak("buat transaksi baru ?(y/t)")
    if transbaru == "y" :
        pilih_dompet()
        if transbaru== "t":
            print ("end")
    


