import submodules
from datetime import date, timedelta

def analisis_keuangan():
    # Identitas subprogram
    print("\n"+"ANALISIS KEUANGAN".center(50,"=")+"\n")

    # Buka dan baca file sejarah_transaksi dan dompet
    hd_dp, ls_dp = submodules.open_read_csv("dompet.csv")
    _, ls_tr = submodules.open_read_csv("sejarah_transaksi.csv")

    # Restriksi 30 hari yg lalu
    hari_ini = date.today()
    hari_30_belakang = (hari_ini - timedelta(days=30)).strftime("%Y/%m/%d")
    ls_tr_new = []
    for ele in ls_tr:
        if ele[0] < hari_30_belakang:
            break
        ls_tr_new.append(ele)

    # Pertambahan/pengurangan dompet
    hd_dp.append("Perubahan")
    for i in range(len(ls_tr_new)):
        _, kode, _, dompet, nominal = ls_tr_new[i]
        nominal = int(nominal)
        tr_index = -1
        for j in range(len(ls_dp)):
            if dompet == ls_dp[j][0]:
                tr_index = j
                break
        try:
            ls_dp[tr_index][2] = ls_dp[tr_index][2] + nominal if kode == "1" else ls_dp[tr_index][2] - nominal
        except IndexError:
            (ls_dp[tr_index]).append(nominal) if kode == "1" else (ls_dp[tr_index]).append(-nominal)
    
    for ele in ls_dp:
        try:
            ele[1] = f"Rp{int(ele[1]):>10,}"
            color2 = "green" if ele[2] >= 0 else "red"
            ele[2] = submodules.ch_color_style(f"Rp{ele[2]:>10,}",color2)
        except IndexError:
            pass

    # Jumlahkan pendapatan berdasarkan tipe dan jumlahkan pengeluaran berdasarkan tipe
    hd_in = ["Income", "Subtotal"]
    ls_in = []
    hd_ex = ["Expenses", "SubTotal", "Percentage"]
    ls_ex = []

    for i in range(len(ls_tr_new)):
        code = ls_tr_new[i][1]
        tipe = ls_tr_new[i][2]
        amount = int(ls_tr_new[i][4])
        
        if tipe == "transfer_akun":
            continue
        
        if code == "1": # Jumlahkan pendapatan berdasarkan tipe pada blok ini
            in_index = -1
            for p in range(len(ls_in)):
                if ls_in[p][0] == tipe:
                    in_index = p
                    break
            if in_index != -1:
                ls_in[in_index][1] += amount
            else:
                ls_in.append([tipe, amount])

        else: # Penjumlahan pengeluaran berdasarkan tipe pada blok ini
            ex_index = -1
            for j in range(len(ls_ex)):
                if ls_ex[j][0] == tipe:
                    ex_index = j
                    break
            if ex_index != -1:
                ls_ex[ex_index][1] += amount
            else:
                ls_ex.append([tipe, amount])

    # Penambahan total semua tipe pendapatan
    total_in = sum([ ele[1] for ele in ls_in ])
    ls_in.append(["Total Slrh", total_in])

    # Penambahan total semua tipe pengeluaran
    total_ex = sum([ ele[1] for ele in ls_ex ])
    ls_ex.append(["Total Slrh", total_ex])

    for ele1 in ls_in:
        ele1[1] = f"Rp{int(ele1[1]):>10,}"
    
    # Presentase pengeluaran pada blok ini
    _, ls_tpex = submodules.open_read_csv("tipe_pengeluaran.csv")
    notes = []

    for j in range(len(ls_ex)-1):
        amount = int(ls_ex[j][1])
        tipe = ls_ex[j][0]
        
        # Default batas presentase pengeluaran per tipe 20 % oleh seluruh pendapatan
        # Ubah presentase tipe apabila ada
        prc = 20
        for k in range(len(ls_tpex)):
            if ls_tpex[k][0] == tipe:
                prc = float(ls_tpex[k][1])

        # Hitung presentase pengeluaran per tipe thd pendapatan
        by_in = round(amount/total_in*100,2)
        ls_ex[j].append(f"{by_in}%")

        ls_ex[j][1] = f"Rp{amount:>10,}"
        
        if by_in > prc:
            for i in range(len(ls_ex[j])):
                ls_ex[j][i] = submodules.ch_color_style(ls_ex[j][i],"red")
            notes.append(f"Pengeluaran tipe {ls_ex[j][0]} berada di atas {prc}% pendapatan bulan ini")
    
    # Untuk total pengeluaran, batas presentase 70% thd seluruh pendapatan
    all_amount = int(ls_ex[-1][1])
    prc_all = 70

    by_in = round(all_amount/total_in*100,2)
    ls_ex[-1].append(f"{by_in}%")

    ls_ex[-1][1] = f"Rp{all_amount:>10,}"
    if by_in > prc_all:
        for i in range(len(ls_ex[-1])):
            ls_ex[-1][i] = submodules.ch_color_style(ls_ex[-1][i],"red")
        notes.append(f"Pengeluaran total berada di atas {prc_all}% pendapatan bulan ini")
    
    # Tampilkan update dompet
    print("Analisis Dompet 30 hari ke belakang :")
    submodules.display_table(ls_dp, hd_dp)
    print()

    # Tampilkan pendapatan berdasarkan tipe
    print("Analisis Pendapatan berdasarkan tipe 30 hari ke belakang :")
    submodules.display_table(ls_in, hd_in)
    print()

    # Tampilkan pengeluaran berdasarkan tipe
    print("Analisis Pengeluaran berdasarkan tipe 30 hari ke belakang :")
    submodules.display_table(ls_ex, hd_ex)
    print()

    # Tampilkan peringatan
    print("Catatan:")
    if len(notes) == 0:
        print("Selamat, tidak ada catatan untuk pengeluaranmu")
    else:
        for ele in notes:
            print(ele)

if __name__ == "__main__":
    analisis_keuangan()