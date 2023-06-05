import submodules

def pilih_dompet():
    while True:
        # Tampilkan nama dompet
        header, list_dompet = submodules.open_read_csv("dompet.csv")
        for nama, nominal in list_dompet:
            print(nama, nominal)
        print("buat")
        
        # Input nama dompet atau buat
        opsi = [ele[0] for ele in list_dompet] + ["buat"]
        pilih = submodules.input_of_options("Pilih dompet kena transaksi atau buat dompet",opsi)
        if pilih != "buat":
            indeks = opsi.index(pilih)
            return list_dompet[indeks][0], int(list_dompet[indeks][1])
        
        # Apabila input buat
        # Masukkan nama dompet
        nama = submodules.input_normal("Masukkan nama dompet : ")
        nominal = submodules.input_money("Masukkan nominal awal dompet : ")

        # Konfirmasi input
        print(f'''Konfirmasi:
Nama dompet  = {nama}
Nominal awal = Rp{nominal:,}''')

        konfir_input = submodules.input_of_yatidak("Apakah mau menyimpan dompet? (y/t) ")

        if konfir_input == "y":
            tulis = [[ nama,nominal ]]
            submodules.open_append_csv("dompet.csv", tulis)

def tulis_dompet(namadompet, code:str, nominal:int):
    header, list_dompet = submodules.open_read_csv("dompet.csv")

    for ele in list_dompet:
        if ele[0] == namadompet:
            ele[1] = int(ele[1]) + nominal if code == "1" else int(ele[1]) - nominal
    
    submodules.open_write_all_csv("dompet.csv",list_dompet, header)

if __name__ == "__main__":
<<<<<<< HEAD
    pilih_dompet()
=======
#     pilih_dompet()
    tulis_dompet(pilih_dompet(),"1",10000)
>>>>>>> 20a55338e2b95eb06af0211380a70c2cf43e192f
