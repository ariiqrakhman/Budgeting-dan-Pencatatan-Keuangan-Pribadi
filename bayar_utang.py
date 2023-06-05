import submodules
<<<<<<< HEAD
from pilih_dompet import pilih_dompet, tulis_dompet
from pemasukan_pengeluaran import rekap_pemasukan_pengeluaran

def bayar_utang(nama:str, dompet:int, nominal:int):
    #membuka file csv 
    header,list_utang = submodules.open_read_csv("utang.csv")
    #memeriksa apakah ada utang dalam daftar
    if len(list_utang >= 1 ):
        #menampilkan daftar utang
        for ele in list_utang:
            print(ele[0], ele[1])
        opsi = [ele[0] for ele in list_utang] + ["keluar"]
        #memilih utang yang akan dibayar
        while True:
            utang_bayar = submodules.input_of_options(prompt='input nama utang atau keluar',opsi)
            if utang_bayar == "keluar":
                print ("konfirmasi keluar")
                return
            #memilih dompet dan nominal
            dompet, nominal = pilih_dompet()




    else:
        print('Output"Tidak ada utang"')




bayar_utang()

# if __name__ == "__main__":
#     bayar_utang("Utang Rakha","umum", 12000)
=======
from pilih_dompet import pilih_dompet
from pemasukan_pengeluaran import rekap_pemasukan_pengeluaran
>>>>>>> 20a55338e2b95eb06af0211380a70c2cf43e192f
