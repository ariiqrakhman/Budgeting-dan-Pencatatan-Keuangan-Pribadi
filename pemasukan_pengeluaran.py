import submodules
from pilih_dompet import pilih_dompet, tulis_dompet
from datetime import date

def rekap_pemasukan_pengeluaran(code:int, tipe:str, dompet:str, nominal:int):
    tanggal = (date.today()).strftime("%Y/%m/%d")

    toadd = [[ tanggal, code, tipe, dompet, nominal ]]

    submodules.open_append2first_csv("sejarah_transaksi.csv", toadd)

    tulis_dompet(dompet, code, nominal)

def pemasukan_pengeluaran():
    while True:
        #pilih dompet
        pilih, nominalawal = pilih_dompet()

        #input 0/1
        inputpp = submodules.input_of_int_options("Pilih pemasukan (1) atau pengeluaran (0) ?", [0,1])

        #masukan nominal pemasukan/pengeluaran
        if inputpp == 1 :
            nominal = submodules.input_money("Masukkan nominal pemasukan :")
            tr = "pemasukan"
        elif inputpp == 0 :
            nominal = submodules.input_money_w_params("Masukkan nominal pengeluaran :", 0, nominalawal)
            tr = "pengeluaran"

        #memilih tipe transaksi
        pilihtipe = pilih_tipe(inputpp)

        # Konfirmasi input
        dis_nom = f"Rp{nominal:,}"

        print(f'''Konfirmasi pembuatan transaksi:
Transaksi {submodules.ch_color_style(tr,"sky")}
Tipe {submodules.ch_color_style(pilihtipe,"sky")}
Nominal {submodules.ch_color_style(dis_nom,"sky")} pada dompet {submodules.ch_color_style(pilih,"sky")}
''')

        #finalisasi pembuatan transaksi
        final = submodules.input_of_yatidak("Finalisasi pembuatan transaksi ?(y/t)")
        if final == "y" :
            rekap_pemasukan_pengeluaran(inputpp, pilihtipe, pilih, nominal)
            break
        elif final == "t" :
            transbaru = submodules.input_of_yatidak("buat transaksi baru ?(y/t)")
            if transbaru == "t":
                break

def pilih_tipe(code:int):
    while True:
        # Konfirmasi tipe yang dipilih sebelumnya
        if code == 1:
            hd, ls_tp = submodules.open_read_csv("tipe_pemasukan.csv")
            tipe = "Pemasukan"
        else:
            hd, ls_tp = submodules.open_read_csv("tipe_pengeluaran.csv")
            tipe = "Pengeluaran"
        
        # Tampilkan tipe yang ada
        dis_ls_tp = [ [id+1] + row for id,row in enumerate(ls_tp) ]
        dis_ls_tp.append([0, "buat"])

        submodules.display_table(dis_ls_tp, [""]+hd)

        # Input pilihan tipe
        banyak_tipe = len(ls_tp)
        opsi = list(range( banyak_tipe+1 ))

        pilih = submodules.input_of_int_options(f"Input 1-{banyak_tipe} untuk pilih tipe {tipe} atau 0 untuk buat tipe ", opsi)

        # Mengembalikan tipe terpilih
        if pilih != 0:
            return ls_tp[pilih-1][0]
        
        # Buat tipe baru apabila input 0
        nama = submodules.input_normal(f"Masukkan nama tipe {tipe}")

        # Konfirmasi tipe baru
        print(f'''Konfirmasi pembuatan tipe {tipe}
    nama tipe = {nama}''')
        
        konfir_input = submodules.input_of_yatidak(f"Apakah mau menyimpan tipe {tipe}? (y/t) ")

        # Apabila input y, simpan dompet
        if konfir_input == "y":
            if code == 1:
                tulis = [[ nama ]]
                submodules.open_append_csv("tipe_pemasukan.csv", tulis)
            else:
                tulis = [[ nama,.3 ]]
                submodules.open_append_csv("tipe_pengeluaran.csv", tulis)

if __name__ == "__main__":
    pemasukan_pengeluaran()
    


