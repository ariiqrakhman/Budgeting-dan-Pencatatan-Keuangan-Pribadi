import matplotlib.pyplot as plt
import submodules

def buat_pdf_4_5():
    hd_tr, ls_tr = submodules.open_read_csv("sejarah_transaksi.csv")

    dict_ty1 = {}
    dict_ty0 = {}

    for ele in ls_tr:
        tgl, kode, tipe, _, nominal = ele
        if tipe == "transfer_akun":
            continue
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
        

    # Prepare data for the donut chart
    label0 = dict_ty0.keys()
    sizes0 = dict_ty0.values()

    # Prepare data for the donut chart
    label1 = dict_ty1.keys()
    sizes1 = dict_ty1.values()

    def create_chart(fig, dis, values, file, nama):
        total = sum(values)

        # Create the donut chart
        plt.figure(fig)
        plt.pie(values, labels=dis, autopct=lambda pct: f"{pct:.2f}% (Rp{round(pct * total / 100,0):,})", wedgeprops={'edgecolor': 'white'})

        # Set aspect ratio to be equal so that pie is drawn as a circle
        plt.axis('equal')

        # Add a white circle in the center to create the donut shape
        center_circle = plt.Circle((0, 0), 0.5, color='white')
        plt.gca().add_artist(center_circle)

        # Display the sum of all sizes below the pie chart
        plt.text(.98, .96, f"Total: Rp{total:,}", ha='center')

        # Judul
        plt.title(nama)

        # plt.show()
        plt.savefig(file+'.pdf')

    create_chart(4, label1, sizes1, "pdf_4", "Distribusi pemasukan dalam 30 hari terakhir")
    create_chart(5, label0, sizes0, "pdf_5", "Distribusi pengeluaran dalam 30 hari terakhir")

if __name__ == "__main__":
    buat_pdf_4_5()