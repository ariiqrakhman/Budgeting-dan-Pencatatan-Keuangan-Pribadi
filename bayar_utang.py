import submodules
from pilih_dompet import pilih_dompet
from pemasukan_pengeluaran import rekap_pemasukan_pengeluaran

def bayar_utang():
    # Identitas subprogram
    print("\n"+"BAYAR UTANG".center(50,"=")+"\n")    

    # Membuka file CSV dan mendapatkan header dan daftar utang
    header, list_utang = sdl.open_read_csv("utang.csv")
    banyak_utang = len(list_utang)

    # Memeriksa apakah ada utang dalam daftar
    if banyak_utang >= 1:
        # Menampilkan daftar utang
        dis_ls_utang = [ [id+1, row[0], f"Rp{int(row[1]):>10,}"] for id,row in enumerate(list_utang) ]
        dis_ls_utang.append([0, "keluar"])

        sdl.display_table(dis_ls_utang, [""]+header)

        # Meminta pengguna untuk memilih utang yang akan dibayar atau keluar dari program
        while True: # Pengulangan permintaan input pilihan utang
            # Meminta input user untuk pemilihan utang dibayar
            opsi = list(range( banyak_utang+1 ))
            if banyak_utang == 1:  
                utang_bayar = sdl.input_of_int_options(f"Input 1 untuk utang dibayar atau 0 untuk keluar", opsi)
            else:  
                utang_bayar = sdl.input_of_int_options(f"Input 1-{banyak_utang} untuk utang dibayar atau 0 untuk keluar", opsi)

            # Apabila user memilih keluar
            if utang_bayar == 0:
                konfir_keluar = sdl.input_of_yatidak("Yakin keluar dari subprogram? (y/t) ")
                if konfir_keluar == "y":
                    print("Keluar dari subprogram")
                    return None # Keluar dari loop dan subprogram
                else:
                    continue
            # Apabila memilih utang dibayar
            elif utang_bayar in opsi:
                nominal_utang = int(list_utang[utang_bayar-1][1]) # Ambil nominal utang terbayar
        
            # Melanjutkan ke langkah selanjutnya: memilih dompet dan nominal pembayaran
            dompet, nominaldompet = pilih_dompet() # Ambil dompet

            # Input nominal bayar utang
            while True:
                try: 
                    dibayar = sdl.input_money_w_params("Masukkan nominal bayar utang? ",0, nominaldompet)
                    assert nominal_utang - dibayar >= 0, f"Nominal bayar terlalu banyak, maksimal {nominal_utang}"
                    break
                except AssertionError as er:
                    print(er)
        
            nominal_utang_dis = f"Rp{nominal_utang:,}"
            dibayar_dis = f"Rp{dibayar:,}"
            # Konfirmasi bayar utang
            print(f'''Konfirmasi bayar utang:
nama utang = {sdl.ch_color_style(list_utang[utang_bayar-1][0],"sky")}
nominal utang = {sdl.ch_color_style(nominal_utang_dis,"sky")}
dibayar = {sdl.ch_color_style(dibayar_dis,"red")} dengan dompet {sdl.ch_color_style(dompet,"sky")}''')
            
            # Apabila konfir bayar utang, keluar dari while loop
            konfir_bayar = sdl.input_of_yatidak("Apakah mau membayar utang? (y/t) ")
            if konfir_bayar == "y":
                break
            # Apabila tidak konfir, kembali mengulang while loop
        
        # Pengurangan utang
        list_utang[utang_bayar-1][1] = nominal_utang - dibayar

        # Apabila sisa utang 0, utang dihapus
        if list_utang[utang_bayar-1][1] == 0:
            list_utang.pop(utang_bayar-1)
        
        # Penulisan file utang
        sdl.open_write_all_csv("utang.csv", list_utang, header)

        # Penulisan rekap pemasukan/pengeluaran
        rekap_pemasukan_pengeluaran(0, "bayar utang", dompet, dibayar)
        
    # Apabila tidak ada utang
    else:
        print('Tidak ada utang')

if __name__ == "__main__":
    bayar_utang()