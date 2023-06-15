import submodules
from datetime import date, timedelta
from os import remove, getcwd
from os.path import join

def invoice():
    # Identitas Subprogram
    print("\n"+"INVOICE".center(50,"=")+"\n")

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
        return

    # Pembuatan baris invoice pertabel
    for id,ele in enumerate(ls_tr_new):
        if ele[1] == "1":
            ls_iv.append([ id+1, ele[0], ele[3], ele[2], sdl.ch_color_style(f"Rp{int(ele[4]):>10,}","green"), None ])
        else:
            ls_iv.append([ id+1, ele[0], ele[3], ele[2], None, sdl.ch_color_style(f"Rp{int(ele[4]):>10,}","red") ])

    # Menampilkan tabel invoice
    print("Daftar transaksi per 30 hari terakhir : ")
    sdl.display_table(ls_iv, hd_iv)

    # Tanya apakah akan membuat invoice pdf
    buat_pdf = sdl.input_of_yatidak("Apakah mau membuat pdf invoice? (y/t) ")
    if buat_pdf == "y":
        from pdf_1 import buat_pdf_1 # Pemanggilan pembuat pdf tabel invoice
        from pdf_2_3 import buat_pdf_2_3 # Pemanggilan pembuatan pdf grafik keuangan
        from pdf_4_5 import buat_pdf_4_5 # Pemanggilan pembuatan pdf chart lingkaran

        buat_pdf_1()
        buat_pdf_2_3()
        buat_pdf_4_5()


        from PyPDF2 import PdfMerger # Mulai penggabungan pdf

        # Daftar file pdf
        pdf_files = ['pdf_1.pdf', 'pdf_2.pdf', 'pdf_3.pdf', 'pdf_4.pdf', 'pdf_5.pdf']

        # Mulai penggabungan pdf
        merger = PdfMerger()

        # Penggabungan pdf pada merger
        for file in pdf_files:
            merger.append(file)

        # Deklarasi nama pdf gabungan
        output_pdf = 'pdf_merge.pdf'

        # Tulis merger ke nama pdf gabungan
        merger.write(output_pdf)

        # Tutup merger
        merger.close()
        
        # Hapus pdf lama
        for ele in pdf_files + ["pdf_2.png", "pdf_3.png"]:
            remove(join(getcwd(),ele))

        # Buka file pdf (Ada kemungkinan tidak berhasil)
        import webbrowser
        pdf_file = 'pdf_merge.pdf'
        webbrowser.open_new_tab(pdf_file)

if __name__ == "__main__":
    invoice()



