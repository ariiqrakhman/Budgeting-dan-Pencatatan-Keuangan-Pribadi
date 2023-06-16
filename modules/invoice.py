from . import submodules as sdl
from datetime import date, timedelta
from os import remove, getcwd, makedirs
from os.path import join

def invoice():
    # Identitas Subprogram
    print("\n"+" INVOICE ".center(50,"=")+"\n")

    # Persiapan tabel invoice
    hd_iv = ["","Tanggal", "Dompet", "Tipe", sdl.ch_color_style("Pemasukan","green"), sdl.ch_color_style("Pengeluaran","red")]
    ls_iv = []

    # Buka file sejarah transaksi
    _ , ls_tr = sdl.open_read_csv("sejarah_transaksi.csv")

    # Restriksi 30 hari yg lalu
    hari_ini = date.today()
    hari_30_belakang = (hari_ini - timedelta(days=30)).strftime("%Y/%m/%d")
    ls_tr_new = []
    for ele in ls_tr:
        if ele[0] < hari_30_belakang:
            break
        ls_tr_new.append(ele)
    
    # Cek transaksi 30 hari ada
    if len(ls_tr_new) == 0:
        print("Kamu belum membuat transaksi 30 hari ini!")
        print("Tidak bisa melakukan pembuatan invoice")
        return # Mengakhiri subprogram karena tidak ada transaksi

    # Pembuatan baris invoice pertabel
    for id,ele in enumerate(ls_tr_new):
        if ele[1] == "1": # untuk pendapatan
            ls_iv.append([ id+1, ele[0], ele[3], ele[2], sdl.ch_color_style(f"Rp{int(ele[4]):>10,}","green"), None ])
        else: # untuk pengeluaran
            ls_iv.append([ id+1, ele[0], ele[3], ele[2], None, sdl.ch_color_style(f"Rp{int(ele[4]):>10,}","red") ])

    # Menampilkan tabel invoice
    print("Daftar transaksi per 30 hari terakhir : ")
    sdl.display_table(ls_iv, hd_iv)

    # Tanya apakah akan membuat invoice pdf
    buat_pdf = sdl.input_of_yatidak("Apakah mau membuat pdf invoice? (y/t) ")
    if buat_pdf == "y":
        from .pdf_1 import buat_pdf_1 # Pemanggilan pembuat pdf tabel invoice
        from .pdf_2_3 import buat_pdf_2_3 # Pemanggilan pembuatan pdf grafik keuangan
        from .pdf_4_5 import buat_pdf_4_5 # Pemanggilan pembuatan pdf chart lingkaran

        output_dir = 'report'

        # Create output directory if it doesn't exist
        makedirs(output_dir, exist_ok=True)


        print("Melakukan pembuatan riwayat, silakan tunggu", end= "\r")
        buat_pdf_1()
        print("Riwayat selesai dibuat                                ")
        print("Melakukan pembuatan grafik, silakan tunggu", end= "\r")
        buat_pdf_2_3()
        print("Grafik selesai dibuat                                  ")
        print("Melakukan chart distribusi riwayat, silakan tunggu", end= "\r")
        buat_pdf_4_5()
        print("Chart distribusi selesai dibuat, silakan tunggu")

        from PyPDF2 import PdfMerger # Mulai penggabungan pdf

        # Daftar file pdf
        pdf_files = ['report/pdf_1.pdf', 'report/pdf_2.pdf', 'report/pdf_3.pdf', 'report/pdf_4.pdf', 'report/pdf_5.pdf']

        # Mulai penggabungan pdf
        print("Menggabungkan konten pdf, silakan tunggu")
        merger = PdfMerger()

        # Penggabungan pdf pada merger
        for file in pdf_files:
            merger.append(file)

        # Deklarasi nama pdf gabungan
        print("Membuat pdf, silakan tunggu")
        tgl_ini = hari_ini.strftime("%Y-%m-%d")
        output_pdf = f'Laporan Keuangan {tgl_ini}.pdf'
        output_path = join(output_dir, output_pdf)

        # Tulis merger ke nama pdf gabungan
        merger.write(output_path)

        # Tutup merger
        merger.close()
        
        # Hapus pdf lama
        for ele in pdf_files + ["report/pdf_2.png", "report/pdf_3.png"]:
            remove(join(getcwd(),ele))

        # Buka file pdf (Ada kemungkinan tidak berhasil)
        print("Membuka pdf")
        import webbrowser
        webbrowser.open_new_tab(output_path)
        print("PDF telah dibuat dan dibuka")