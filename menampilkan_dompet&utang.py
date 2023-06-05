import submodules
from datetime import date

def menampilkan_dompet_utang():
    today_dp = (date.today()).strftime("%d/%m/%Y")
    today_rd = (date.today()).strftime("%Y/%m/%d")

    headertrans, listrans = submodules.open_read_csv("sejarah_transaksi.csv")
    trans_today_add = sum([ele[1] for ele in listrans if ele[0] == today_rd and ele[2] == "1"])
    trans_today_min = sum([ele[1] for ele in listrans if ele[0] == today_rd and ele[2] == "0"])

    headerdompet, listdompet = submodules.open_read_csv("dompet.csv")
    headerutang, listutang = submodules.open_read_csv("utang.csv")

    print(submodules.display_table_centered(listdompet, headerdompet))
    print(submodules.display_table_centered(listutang, headerutang))

menampilkan_dompet_utang()