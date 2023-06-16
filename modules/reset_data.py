from . import submodules as sdl

hd_dp, _ = sdl.open_read_csv("dompet.csv")
hd_tr, _ = sdl.open_read_csv("sejarah_transaksi.csv")
hd_ut, _ = sdl.open_read_csv("utang.csv")
hd_tp_1, ls_tp_1 = sdl.open_read_csv("tipe_pemasukan.csv") 
hd_tp_0, ls_tp_0 = sdl.open_read_csv("tipe_pengeluaran.csv")

sdl.open_write_all_csv("dompet.csv", [], hd_dp)
sdl.open_write_all_csv("sejarah_transaksi.csv", [], hd_tr)
sdl.open_write_all_csv("utang.csv", [], hd_ut)

ls_tp_1 = [["gaji"],
            ["uang saku"],
            ["bonus/hadiah"],
            ["parttime"],
            ["dan lain-lain"]
            ]

ls_tp_0 = [
            ["makan",25.0],
            ["jajan",25.0],
            ["transportasi",25.0],
            ["rekreasi",25.0],
            ["hadiah",25.0],
            ["komunikasi",25.0],
            ["dan lain-lain",25.0]
            ]

sdl.open_write_all_csv("tipe_pemasukan.csv", ls_tp_1, hd_tp_1)
sdl.open_write_all_csv("tipe_pengeluaran.csv", ls_tp_0, hd_tp_0)
