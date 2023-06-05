import submodules
from pilih_dompet import pilih_dompet, tulis_dompet
from datetime import date

def rekap_pemasukan_pengeluaran(kode:str, tipe:str, dompet:str, nominal:int):
    tanggal = (date.today()).strftime("%Y/%m/%d")

    toadd = [[ tanggal, kode, tipe, dompet, nominal ]]

    submodules.open_append_csv("sejarah_transaksi.csv", toadd)

    tulis_dompet(dompet, kode, nominal)

def pemasukan_pengeluaran():
    while True:
        #pilih dompet
        pilih, nominalawal = pilih_dompet()
        #input 0/1
        inputpp = submodules.input_of_options("Pilih pemasukan (1) atau pengeluaran (0) ?",['0','1'])
        #masukan nominal pemasukan/pengeluaran
        if inputpp == "1" :
            nominal = submodules.input_money("Masukkan nominal pemasukan :")
        elif inputpp == "0" :
            nominal = submodules.input_money_w_params("Masukkan nominal pengeluaran :", "0", nominalawal)
        #memilih tipe transaksi
        ls_tipe = submodules.open_read_csv("tipe.csv")
        if inputpp == "1" :
            tipe = [tp[1] for tp in ls_tipe if tp[0]=="1"]
        elif inputpp == "0" :
            tipe = [tp[1] for tp in ls_tipe if tp[0]=="0"]
        pilihtipe = submodules.input_of_options("Pilih tipe transaksi :", tipe)
        #finalisasi pembuatan transaksi
        final = submodules.input_of_yatidak("Finalisasi pembuatan transaksi ?(y/t)")
        if final == "y" :
            rekap_pemasukan_pengeluaran(inputpp, pilihtipe, pilih, nominal)
        elif final == "t" :
            transbaru = submodules.input_of_yatidak("buat transaksi baru ?(y/t)")
            if transbaru == "t":
                break

if __name__ == "__main__":
    rekap_pemasukan_pengeluaran("0", "dll", "umum", 40000)
    


