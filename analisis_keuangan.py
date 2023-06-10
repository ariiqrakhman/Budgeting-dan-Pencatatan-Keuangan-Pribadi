import submodules
from datetime import date

def analisis_keuangan():
    # Buka dan baca file sejarah_transaksi dan domepet
    hd_dp, ls_dp = submodules.open_read_csv("dompet.csv")
    hd_tr, ls_tr = submodules.open_read_csv("sejarah_transaksi.csv")

    # Restriksi bulan ini
    hari_ini = date.today()
    bulan_ini = hari_ini.strftime("%Y/%m")
    ls_tr_new = []
    for ele in ls_tr:
        if not ele[0].startswith(bulan_ini):
            break
        ls_tr_new.append(ele)

    # Pertambahan/pengurangan dompet
    hd_dp.append("Perubahan")
    for i in range(len(ls_tr_new)):
        kode = ls_tr_new[i][1]
        dompet = ls_tr_new[i][3]
        nominal = int(ls_tr_new[i][4])
        tr_index = -1
        for j in range(len(ls_dp)):
            if dompet == ls_dp[j][0]:
                tr_index = j
                break
        try:
            ls_dp[tr_index][2] = ls_dp[tr_index][2] + nominal if kode == "1" else ls_dp[tr_index][2] - nominal
        except IndexError:
            (ls_dp[tr_index]).append(nominal) if kode == "1" else (ls_dp[tr_index]).append(-nominal)

    # Jumlahkan pendapatan dan jumlahkan pengeluaran berdasarkan tipe
    hd_ex = ["Expenses", "Total", "Percentage"]
    ls_ex = []
    total_pendapatan = 0
    for i in range(len(ls_tr_new)):
        code = ls_tr_new[i][1]
        type = ls_tr_new[i][2]
        amount = int(ls_tr_new[i][4])
        # Jumlahkan pendapatan pada blok ini
        if code == "1":
            total_pendapatan += amount
        # Penjumlahan pengeluaran berdasarkan tipe pada blok ini
        else:
            ex_index = -1
            for j in range(len(ls_ex)):
                if ls_ex[j][0] == type:
                    ex_index = j
                    break
            if ex_index != -1:
                ls_ex[ex_index][1] += amount
            else:
                ls_ex.append([type, amount])
    
    # Presentase pengeluaran pada blok ini
    notes = []
    for j in range(len(ls_ex)):
        amount = ls_ex[j][1]
        prc = round(amount/total_pendapatan*100,2)
        (ls_ex[j]).append(prc)
        if prc > 30:
            for i in range(len(ls_ex[j])):
                ls_ex[j][i] = submodules.ch_color_style(ls_ex[j][i],"red")
            notes.append(f"Pengeluaran tipe {ls_ex[j][0]} berada di atas 30% pendapatan bulan ini")
    
    # Tampilkan update dompet
    submodules.display_table(ls_dp, hd_dp)

    # Tampilkan pengeluaran berdasarkan tipe
    submodules.display_table(ls_ex, hd_ex)

    # Tampilkan peringatan
    print("Catatan:")
    if len(notes) == 0:
        print("Selamat, tidak ada catatan untuk pengeluaranmu")
    else:
        for ele in notes:
            print(ele)

if __name__ == "__main__":
    analisis_keuangan()

            


