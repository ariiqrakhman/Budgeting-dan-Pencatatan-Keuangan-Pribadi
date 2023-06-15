import matplotlib.pyplot as plt
import submodules
from datetime import date, timedelta

def buat_pdf_4_5():
    # Pembacaan file sejarah_transaksi
    _, ls_tr = submodules.open_read_csv("sejarah_transaksi.csv")

    # Persiapan pembuatan x-y key-value untuk distribusi pendapatan
    dict_ty1 = {}
    # Persiapan pembuatan x-y key-value untuk distribusi pengeluaran
    dict_ty0 = {}

    # Restriksi 30 hari ke belakang
    current_date = date.today()
    date_30_back = (current_date - timedelta(days=30)).strftime("%Y/%m/%d")

    # pengisian x-y
    for ele in ls_tr:
        tgl, kode, tipe, _, nominal = ele
        # Distribusi tidak melibatkan tipe transfer
        if tipe == "transfer_akun": 
            continue
        # Distribusi hanya pada 30 hari terakhir
        if tgl < date_30_back:
            break
        if kode == "1":
            if tipe not in dict_ty1:
                dict_ty1[tipe] = int(nominal)
            else:
                dict_ty1[tipe] += int(nominal)
        else:
            if tipe not in dict_ty0:
                dict_ty0[tipe] = int(nominal)
            else:
                dict_ty0[tipe] += int(nominal)

    # Label dan ukuran untuk distribusi pengeluaran
    label0 = dict_ty0.keys()
    sizes0 = dict_ty0.values()

    # Label dan ukuran untuk distribusi pendapatan
    label1 = dict_ty1.keys()
    sizes1 = dict_ty1.values()

    # Pembuatan pie chart
    def create_chart(fig, dis, values, file, nama):
        total = sum(values)

        plt.figure(fig)
        plt.pie(values, labels=dis, autopct=lambda pct: f"{pct:.2f}% (Rp{round(pct * total / 100,0):,})", wedgeprops={'edgecolor': 'white'})

        plt.axis('equal')

        center_circle = plt.Circle((0, 0), 0.5, color='white')
        plt.gca().add_artist(center_circle)

        plt.text(.98, .96, f"Total: Rp{total:,}", ha='center')

        plt.title(nama)

        # plt.show()
        plt.savefig(file+'.pdf')

    # Pembuatan pie chart untuk distribusi pemasukan
    create_chart(4, label1, sizes1, "pdf_4", "Distribusi pemasukan dalam 30 hari terakhir")
    # Pembuatan pie chart untuk distribusi pengeluaran
    create_chart(5, label0, sizes0, "pdf_5", "Distribusi pengeluaran dalam 30 hari terakhir")

if __name__ == "__main__":
    buat_pdf_4_5()