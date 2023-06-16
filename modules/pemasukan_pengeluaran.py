from . import submodules as sdl
from .pilih_dompet import pilih_dompet, tulis_dompet
from .edit_tipe import pilih_tipe
from datetime import date

def rekap_pemasukan_pengeluaran(code:int, tipe:str, dompet:str, nominal:int):
    # Akses tanggal pembuatan transaksi (hari ini)
    tanggal = (date.today()).strftime("%Y/%m/%d")

    # Persiapan list ditulis ke csv
    toadd = [[ tanggal, code, tipe, dompet, nominal ]]

    # Penulisan ke csv pada index value pertama
    sdl.open_append2first_csv("sejarah_transaksi.csv", toadd)

    # Penulisan/overwriting dompet
    tulis_dompet(dompet, code, nominal)

def pemasukan_pengeluaran():
    while True: # Pengulangan selama belum keluar subprogram
        # Identitas Subprogram
        print("\n"+"PEMASUKAN PENGELUARAN".center(50,"=")+"\n")    

        #pilih dompet
        pilih, nominalawal = pilih_dompet()

        #input 0/1
        inputpp = sdl.input_of_int_options("Pilih pemasukan (1) atau pengeluaran (0) ?", [0,1])

        #masukan nominal pemasukan/pengeluaran
        if inputpp == 1 :
            nominal = sdl.input_money("Masukkan nominal pemasukan :")
            clr = "sky"
            tr = "pemasukan"
        elif inputpp == 0 :
            nominal = sdl.input_money_w_params("Masukkan nominal pengeluaran :", 0, nominalawal)
            if nominal == None:
                print(sdl.ch_color_style("Uang tidak cukup, dialihkan kembali ke menu utama\n","yellow"))
                return # Ketika nominal pengeluaran gagal didapatkan
            clr = "red"
            tr = "pengeluaran"

        #memilih tipe transaksi
        pilihtipe = pilih_tipe(inputpp)

        # Konfirmasi input
        dis_nom = f"Rp{nominal:,}"

        print(f'''Konfirmasi pembuatan transaksi:
Transaksi {sdl.ch_color_style(tr,clr)}
Tipe {sdl.ch_color_style(pilihtipe,clr)}
Nominal {sdl.ch_color_style(dis_nom,clr)} pada dompet {sdl.ch_color_style(pilih,"sky")}
''')

        # finalisasi pembuatan transaksi
        final = sdl.input_of_yatidak("Finalisasi pembuatan transaksi ?(y/t)")
        if final == "y" : # Jika konfir input diterima
            rekap_pemasukan_pengeluaran(inputpp, pilihtipe, pilih, nominal)
            break
        # Apakah mau melanjutkan subprogram
        elif final == "t" : # Jika konfir input tidak diterima
            transbaru = sdl.input_of_yatidak("buat transaksi baru? (input t untuk keluar dari subprogram) (y/t)")
            if transbaru == "t":
                break

if __name__ == "__main__":
    pemasukan_pengeluaran()
    


