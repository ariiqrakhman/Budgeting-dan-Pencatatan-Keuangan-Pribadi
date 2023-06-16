from . import submodules as sdl

def buat_tipe(code:int):
    # Konfirmasi tipe yang dipilih sebelumnya
    if code == 1:
        tp = "Pemasukan"
    else:
        tp = "Pengeluaran"
    # Buat tipe baru apabila input 0
    nama = sdl.input_normal(f"Masukkan nama tipe {tp}")

    # Konfirmasi tipe baru
    print(f'''Konfirmasi pembuatan tipe {tp}
nama tipe = {sdl.ch_color_style(nama,"sky")}''')
        
    konfir_input = sdl.input_of_yatidak(f"Apakah mau menyimpan tipe {tp}? (y/t) ")

    # Apabila input y, simpan tipe
    if konfir_input == "y":
        if code == 1:
            tulis = [[ nama ]]
            sdl.open_append_csv("tipe_pemasukan.csv", tulis)
        else:
            tulis = [[ nama, 25 ]]
            sdl.open_append_csv("tipe_pengeluaran.csv", tulis)

def pilih_tipe(code:int):
    while True:
        # Konfirmasi tipe yang dipilih sebelumnya
        if code == 1:
            hd, ls_tp = sdl.open_read_csv("tipe_pemasukan.csv")
            dis_ls_tp = [ [id+1] + row for id,row in enumerate(ls_tp) ]
            tipe = "Pemasukan"
        else:
            hd, ls_tp = sdl.open_read_csv("tipe_pengeluaran.csv")
            dis_ls_tp = [ [id+1, row[0]] for id,row in enumerate(ls_tp) ]
            tipe = "Pengeluaran"
        
        # Tampilkan tipe yang ada
        dis_ls_tp.append([0, "buat"])

        print("Daftar Tipe dapat dipilih: ")
        sdl.display_table(dis_ls_tp, [""]+hd)

        # Input pilihan tipe
        banyak_tipe = len(ls_tp)
        opsi = list(range( banyak_tipe+1 ))

        pilih = sdl.input_of_int_options(f"Input 1-{banyak_tipe} untuk pilih tipe {tipe} atau 0 untuk buat tipe ", opsi)

        # Mengembalikan tipe terpilih
        if pilih != 0:
            return ls_tp[pilih-1][0]
        
        # Apabila input 0 / buat tipe
        buat_tipe(code)

def edit_tipe():
    while True: # Pengulangan subprogram kecuali user keluar
        # Identitas subprogram
        print("\n"+"EDIT TIPE".center(50,"=")+"\n")

        # Mengakses masing-masing tipe pendapatan dan pengeluaran 
        hd_in, ls_in = sdl.open_read_csv("tipe_pemasukan.csv")
        hd_ex, ls_ex = sdl.open_read_csv("tipe_pengeluaran.csv")

        byk_tipe1 = len(ls_in)
        ls_in_dis = [ [id+1] + row for id,row in enumerate(ls_in)]

        byk_tipe2 = len(ls_ex)
        ls_ex_dis = [ [id+1+byk_tipe1] + row for id,row in enumerate(ls_ex) ]

        # Menampilkan daftar tipe pemasukan
        print("Daftar Tipe Pemasukan :")
        sdl.display_table(ls_in_dis, [""] + hd_in)

        # Menampilkan daftar tipe pemasukan
        print("Daftar Tipe pengeluaran :")
        sdl.display_table(ls_ex_dis, [""] + hd_ex)

        # Tampilan menu subprogram
        print("")
        print("""Pilih menu subprogram:
1. Buat tipe baru
2. Hapus tipe
3. Edit batas presentase pengeluaran
4. Keluar dari subprogram""")
        
        # Input pilihan menu dari user
        pilih_menu = sdl.input_of_int_options("Silakan pilih menu 1,2,3,4", [1,2,3,4])

        # Pilihan buat tipe baru
        if pilih_menu == 1:
            kode = sdl.input_of_int_options("Pilih buat tipe pemasukan (1) atau tipe pengeluaran (0) ", [0,1])
            buat_tipe(kode)

        # Pilihan menghapus tipe yg ada
        elif pilih_menu == 2:
            pilih_label = sdl.input_of_int_options(f"Input nomor tipe (1-{byk_tipe1+byk_tipe2}) yang ingin dihapus ", list(range(1,byk_tipe1+byk_tipe2+1)) )
            
            # Menghapus tipe pemasukan/pemasukan berdasarkan var pilih_label
            if pilih_label <= byk_tipe1:
                tipe_dihapus = ls_in[pilih_label-1][0]
                dari = "Pemasukan"
            else:
                tipe_dihapus = ls_ex[pilih_label-byk_tipe1-1][0]
                dari = "Pengeluaran"
            
            # Konfirmasi hapus tipe
            print(f"""Konfirmasi hapus tipe:
Tipe {sdl.ch_color_style(tipe_dihapus, "blue")} dari {sdl.ch_color_style(dari, "blue")}""")

            konfir_hapus = sdl.input_of_yatidak("Yakin ingin menghapus tipe? (y/t) ")
            # Jika konfir diterima, hapus tipe dan tulis ulang file tipe
            if konfir_hapus == "y":
                if pilih_label <= byk_tipe1:
                    ls_in.pop(pilih_label-1)
                    sdl.open_write_all_csv("tipe_pemasukan.csv", ls_in, hd_in)
                else:
                    ls_ex.pop(pilih_label-byk_tipe1-1)
                    sdl.open_write_all_csv("tipe_pengeluaran.csv", ls_ex, hd_ex)
            # Kembali ke menu subprogram

        # Pilihan menu edit batas presentase pengeluaran
        elif pilih_menu == 3:
            # Pilih pengeluaran yg ada
            pilih_label = sdl.input_of_int_options(f"Input nomor tipe pengeluaran ({byk_tipe1+1}-{byk_tipe1+byk_tipe2}) yang ingin diganti batas presentase pengeluaran ", list(range(byk_tipe1+1,byk_tipe1+byk_tipe2+1)) )
            
            # Tanyakan presentase baru yg diharapkan
            while True:
                try:
                    prc_baru = float(input("Masukkan batas presentase baru (Contoh Input: 90, 75, 55.5) \n"))
                    assert prc_baru >= 0 and prc_baru <= 100, "Presentase salah!"
                    break
                except AssertionError as er:
                    print(er)
                except ValueError:
                    print("Input tidak Valid!")
            
            # Konfirmasi input perubahan presentase
            dis_prc_baru = f"{prc_baru}%"
            print(f"""Konfirmasi ubah batas presentase:
Nama tipe pengeluaran {sdl.ch_color_style(ls_ex[pilih_label-byk_tipe1-1][0],"blue")}
Batas presentase baru {sdl.ch_color_style(dis_prc_baru,"blue")}""")
            
            konfir_ganti = sdl.input_of_yatidak("Yakin ingin menyimpan perubahan? (y/t) ")
            # apabila konfir diterima, ubah presentase dari tipe terpilih dan tulis ulang file tipe
            if konfir_ganti == "y":
                ls_ex[pilih_label-byk_tipe1-1][1] = prc_baru
                sdl.open_write_all_csv("tipe_pengeluaran.csv", ls_ex, hd_ex)
        
        # Pilihan untuk keluar dari subprogram
        elif pilih_menu == 4:
            konfir_keluar = sdl.input_of_yatidak("Yakin ingin keluar dari subprogram? (y/t) ")
            if konfir_keluar == "y":
                return # Keluar dari subprogram

if __name__ == "__main__":
    edit_tipe()

