from . import submodules as sdl
from .pemasukan_pengeluaran import rekap_pemasukan_pengeluaran

def transfer_akun():
    # Akses file dompet
    hd_dompet, ls_dompet = sdl.open_read_csv("dompet.csv")
    byk_dompet = len(ls_dompet)

    if byk_dompet < 2:
        print("Setidaknya memiliki 2 dompet untuk melakukan transfer akun")
        return # Kembali karena banyak dompet tidak cukup
    
    # Tampilkan dompet
    dis_tl = [ [id+1, row[0], f"Rp{int(row[1]):^12,}"] for id,row in enumerate(ls_dompet) ]
    sdl.display_table(dis_tl, [""] + hd_dompet)

    opsi = list(range(1,byk_dompet+1))
    lbl_1 = sdl.input_of_int_options(f"Input 1-{byk_dompet} untuk memilih dompet pemberi transfer ", opsi)
    dompet_1, nominal_1 = ls_dompet[lbl_1-1][0], int(ls_dompet[lbl_1-1][1]) # Ambil dompet 1

    nominal_tf = sdl.input_money_w_params(f"Masukkan jumlah uang ditransfer ",0, nominal_1)
    if nominal_tf == None:
        print(sdl.ch_color_style("Uang tidak cukup, dikembalikan ke menu utama","yellow"))
        return # Ketika nominal pengeluaran gagal didapatkan

    opsi.remove(lbl_1) # Hapus pilihan dompet satu untuk persiapan input dompet kedua
    lbl_2 = sdl.input_of_int_options(f"Input 1-{byk_dompet} untuk memilih dompet penerima transfer ", opsi, f"Pilih dompet yang ada kecuali dompet {dompet_1}!")
    dompet_2, nominal_2 = ls_dompet[lbl_2-1][0], int(ls_dompet[lbl_2-1][1]) # ambil dompet 2

    adm = sdl.input_money("Masukkan biaya admin, input 0 jika tidak ada")

    if adm > 0:
        # Jika biaya admin ada
        print("Opsi dompet terkena admin")
        print(f"1. {dompet_1}")
        print(f"2. {dompet_2}")
        count = 0
        while True:
            try:
                if count >= 3:
                    print(sdl.ch_color_style("Uang tidak cukup, kembali ke menu utama","yellow"))
                    return # Ketika tidak didapatkan siapa dompet kena admin
                kena_adm = sdl.input_of_int_options("Dompet mana yang terkena admin? ", [1,2])
                count += 1
                assert nominal_1 - nominal_tf - adm >= 0 if kena_adm == 1 \
                    else nominal_2 - nominal_tf - adm >= 0, "Uang tidak cukup!"
            except AssertionError as er:
                print(er)
    else:
        kena_adm = 0 # Tidak ada biaya admin

    nominal_dis = f"Rp{nominal_tf:,}"
    print(f'''Konfirmasi transfer akun :
Transfer sebanyak {sdl.ch_color_style(nominal_dis, "sky")}
Dari {sdl.ch_color_style(dompet_1, "sky")}
ke {sdl.ch_color_style(dompet_2, "sky")}''')
            
    if adm > 0:
        if kena_adm == 1:
            print(f'Biaya admin {sdl.ch_color_style(f"Rp{adm:,}", "red")} pada {dompet_1}')
        elif kena_adm == 2:
            print(f'Biaya admin {sdl.ch_color_style(f"Rp{adm:,}", "red")} pada {dompet_2}')

    konfir = sdl.input_of_yatidak(f"Yakin melakukan transfer akun? (y/t) ")
    if konfir == "y":
        rekap_pemasukan_pengeluaran(0, "transfer_akun", dompet_1, nominal_tf)

        rekap_pemasukan_pengeluaran(1, "transfer_akun", dompet_2, nominal_tf)

        if kena_adm == 1:
            rekap_pemasukan_pengeluaran(0, "dan lain-lain", dompet_1, adm)

        elif kena_adm == 2:
            rekap_pemasukan_pengeluaran(0, "dan lain-lain", dompet_2, adm)

if __name__ == "__main__":
    transfer_akun()



