import submodules

def invoice():
    hd_iv = ["Tanggal", "Dompet", "Tipe", "Pemasukan", "Pengeluaran"]
    ls_iv = []

    hd_tr, ls_tr = submodules.open_read_csv("sejarah_transaksi.csv")

    for ele in ls_tr:
        if ele[1] == "1":
            ls_iv.append([ ele[0], ele[3], ele[2], ele[4], None ])
        else:
            ls_iv.append([ ele[0], ele[3], ele[2], None, ele[4] ])

    # for ele in ls_iv:
    #     print(ele)
    submodules.display_table(ls_iv, hd_iv)

if __name__ == "__main__":
    invoice()



