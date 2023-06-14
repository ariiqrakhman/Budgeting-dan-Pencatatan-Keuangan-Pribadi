import submodules
from pemasukan_pengeluaran import rekap_pemasukan_pengeluaran

def transfer_akun():
    # Akses file dompet
    hd_dompet, list_dompet = submodules.open_read_csv("dompet.csv")
    banyak_dompet = len(list_dompet)

    if banyak_dompet < 2:
        print("Setidaknya memiliki 2 dompet untuk melakukan transfer akun")
        return
    
    # Tampilkan dompet
    dis_tl = [ [id+1, row[0], f"Rp{int(row[1]):^12,}"] for id,row in enumerate(list_dompet) ]
    submodules.display_table(dis_tl, [""] + hd_dompet)

    opsi = list(range(1,banyak_dompet+1))
    lbl_1 = submodules.input_of_int_options(f"Input 1-{banyak_dompet} untuk memilih dompet pemberi transfer ", opsi)
    dompet_1, nominal_1 = list_dompet[lbl_1-1][0], int(list_dompet[lbl_1-1][1])

    nominal_tf = submodules.input_money_w_params(f"Masukkan jumlah uang ditransfer ",0, nominal_1)

    opsi.remove(lbl_1)
    lbl_2 = submodules.input_of_int_options(f"Input 1-{banyak_dompet} untuk memilih dompet penerima transfer ", opsi, f"Pilih dompet yang ada kecuali dompet {dompet_1}!")
    dompet_2, nominal_2 = list_dompet[lbl_2-1][0], int(list_dompet[lbl_2-1][1])

    adm = submodules.input_money("Masukkan biaya admin, input 0 jika tidak ada")

    if adm > 0:
        print(f"1. {dompet_1}\n2. {dompet_2}")
        kena_adm = submodules.input_of_int_options("Dompet mana yang terkena admin? ", [1,2])
    else:
        kena_adm = 0

    nominal_dis = f"Rp{nominal_tf:,}"
    print(f"""Konfirmasi transfer akun :
Transfer sebanyak {submodules.ch_color_style(nominal_dis, "sky")}
Dari {submodules.ch_color_style(dompet_1, "sky")}
ke {submodules.ch_color_style(dompet_2, "sky")}""")
            
    if adm > 0:
        if kena_adm == 1:
            print(f'Biaya admin {submodules.ch_color_style(f"Rp{adm:,}", "red")} pada {dompet_1}')
        elif kena_adm == 2:
            print(f'Biaya admin {submodules.ch_color_style(f"Rp{adm:,}", "red")} pada {dompet_2}')

    konfir = submodules.input_of_yatidak(f"Yakin melakukan transfer akun? (y/t) ")
    if konfir == "y":
        nominal_1 -= nominal_tf
        rekap_pemasukan_pengeluaran(0, "transfer_akun", dompet_1, nominal_tf)

        nominal_2 += nominal_tf
        rekap_pemasukan_pengeluaran(1, "transfer_akun", dompet_2, nominal_tf)

        if kena_adm == 1:
            nominal_1 -= adm
            rekap_pemasukan_pengeluaran(0, "dan lain-lain", dompet_1, adm)

        elif kena_adm == 2:
            nominal_2 -= adm
            rekap_pemasukan_pengeluaran(0, "dan lain-lain", dompet_2, adm)

if __name__ == "__main__":
    transfer_akun()



