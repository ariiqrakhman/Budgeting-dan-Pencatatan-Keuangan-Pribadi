import submodules
from datetime import date

def invoice():
    hd_iv = ["","Tanggal", "Dompet", "Tipe", submodules.ch_color_style("Pemasukan","green"), submodules.ch_color_style("Pengeluaran","red")]
    ls_iv = []

    hd_tr, ls_tr = submodules.open_read_csv("sejarah_transaksi.csv")

    # Restriksi bulan ini
    hari_ini = date.today()
    bulan_ini = hari_ini.strftime("%Y/%m")
    ls_tr_new = []
    for ele in ls_tr:
        if not ele[0].startswith(bulan_ini):
            break
        ls_tr_new.append(ele)

    # Pembuatan baris invoice pertabel
    for id,ele in enumerate(ls_tr_new):
        if ele[1] == "1":
            ls_iv.append([ id+1, ele[0], ele[3], ele[2], submodules.ch_color_style(f"Rp{int(ele[4]):^12,}","green"), None ])
        else:
            ls_iv.append([ id+1, ele[0], ele[3], ele[2], None, submodules.ch_color_style(f"Rp{int(ele[4]):^12,}","red") ])

    # Menampilkan tabel invoice
    submodules.display_table(ls_iv, hd_iv)

    # Tanya apakah akan membuat invoice pdf
    buat_pdf = submodules.input_of_yatidak("Apakah mau membuat pdf invoice? (y/t) ")
    if buat_pdf == "y":
        pass

if __name__ == "__main__":
    invoice()



