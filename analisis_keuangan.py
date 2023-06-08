import submodules
from datetime import date

def analisis_keuangan():
    # Buka dan baca file sejarah_transaksi dan domepet
    hd_dp, ls_dp = submodules.open_read_csv("dompet.csv")
    hd_tr, ls_tr = submodules.open_read_csv("sejarah_transaksi.csv")

    # Pertambahan/pengurangan dompet
    hd_dp.append("Perubahan")
    for i in range(len(ls_tr)):
        kode = ls_tr[i][1]
        dompet = ls_tr[i][3]
        nominal = int(ls_tr[i][4])
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
    for i in range(len(ls_tr)):
        code = ls_tr[i][1]
        type = ls_tr[i][2]
        amount = int(ls_tr[i][4])
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
    for j in range(len(ls_ex)):
        amount = ls_ex[j][1]
        (ls_ex[j]).append(round(amount/total_pendapatan*100,2))
    
    # Tampilkan update dompet
    submodules.display_table(ls_dp, hd_dp)

    # Tampilkan pengeluaran berdasarkan tipe
    submodules.display_table(ls_ex, hd_ex)

if __name__ == "__main__":
    analisis_keuangan()

            


