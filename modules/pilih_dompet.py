from . import submodules as sdl

def pilih_dompet():
    while True:
        # Buka file dompet
        hd_dompet, ls_dompet = sdl.open_read_csv("dompet.csv")

        # Persiapan Tampilan nama dan nominal dompet
        dis_tl = [ [id+1, row[0], f"Rp{int(row[1]):^12,}"] for id,row in enumerate(ls_dompet) ]
        dis_tl.append([0, "buat"])
        
        # Input nama dompet atau buat
        banyak_dompet = len(ls_dompet)
        opsi = list(range( banyak_dompet+1 ))
        # Jika belum punya dompet, diarahkan untuk buat dompet baru
        if banyak_dompet == 0:
            print("Anda belum punya dompet!")
            print("Diarahkan ke bagian buat dompet")
            pilih = 0
        
        # Jika sudah ada dompet, dompet dan nominalnya ditampilkan
        elif banyak_dompet == 1:
            print("Daftar dompet dapat dipilih :")
            sdl.display_table(dis_tl, [""] + hd_dompet)
            pilih = sdl.input_of_int_options(f"Input 1 untuk pilih dompet atau 0 untuk buat dompet ",opsi)
        
        elif banyak_dompet > 1:
            print("Daftar dompet dapat dipilih :")
            sdl.display_table(dis_tl, [""] + hd_dompet)
            pilih = sdl.input_of_int_options(f"Input 1-{banyak_dompet} untuk pilih dompet atau 0 untuk buat dompet ",opsi)

        # Apabila nama dompet terpilih, kembalikan dompet terpilih dan tutup subprogram
        if pilih != 0:
            return ls_dompet[pilih-1][0], int(ls_dompet[pilih-1][1])
        
        # Apabila input 0 (buat),
        # Masukkan nama dompet
        nama = sdl.input_normal("Masukkan nama dompet : ")
        
        print(f'''Konfirmasi pembuatan dompet:
Nama dompet  = {sdl.ch_color_style(nama,"sky")}''')
        
        # Konfirmasi penyimpanan dompet baru
        konfir_input = sdl.input_of_yatidak("Apakah mau menyimpan dompet? (y/t) ")

        # Apabila input y, simpan dompet
        if konfir_input == "y":
            tulis = [[ nama, 0 ]]
            sdl.open_append_csv("dompet.csv", tulis)

def tulis_dompet(namadompet, code:int, nominal:int):
    # Buka file dompet
    header, ls_dompet = sdl.open_read_csv("dompet.csv")

    # Sesuai kode, ubah nominal dari dompet terpilih
    for ele in ls_dompet:
        if ele[0] == namadompet:
            ele[1] = int(ele[1]) + nominal if code == 1 else int(ele[1]) - nominal
    
    # Tulis perubahan pada file dompet kembali
    sdl.open_write_all_csv("dompet.csv",ls_dompet, header)