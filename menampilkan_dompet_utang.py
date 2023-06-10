import submodules

def menampilkan_dompet_utang():
    # Akses file domept dan file utang
    hd_dompet , ls_dompet = submodules.open_read_csv("dompet.csv")
    hd_utang , ls_utang = submodules.open_read_csv("utang.csv")

    # Tampilkan dompet
    if len(ls_dompet) >= 1:
        submodules.display_table(ls_dompet, hd_dompet)
    else:
        print("\nKamu belum memiliki dompet")

    # Tampilkan utang
    if len(ls_utang) >= 1:
        submodules.display_table(ls_utang, hd_utang)
    else:
        print("\nSelamat, Kamu tidak memiliki utang!")

if __name__ == "__main__":
    menampilkan_dompet_utang()