import matplotlib.pyplot as plt
from reportlab.pdfgen import canvas
import datetime
import submodules

def buat_pdf_2_3():
    # dapatkan tanggal hari ini
    current_date = datetime.date.today()

    # list tanggal 30 hari ke belakang
    date_list = []

    # Restriksi 30 hari ke belakang
    for i in range(30, -1, -1):
        date = current_date - datetime.timedelta(days=i)
        date_list.append(date.strftime("%Y/%m/%d"))

    # Pembuatan nilai tren pemasukan-pengeluaran
    _, ls_tr = submodules.open_read_csv("sejarah_transaksi.csv")
    money_flow = []
    for date in (date_list):
        money_flow_on_date = 0
        for baris in ls_tr:
            date_str, kode, _, _, nominal = baris
            kode, nominal = int(kode), int(nominal)
            if date == date_str:
                money_flow_on_date = money_flow_on_date + nominal if kode == 1 else money_flow_on_date - nominal
            elif date > date_str:
                break
        money_flow.append(money_flow_on_date)
    
    # Pembuatan nilai perubahan aset
    _, ls_dp = submodules.open_read_csv("dompet.csv")
    sum_dp = sum([int(ele[1]) for ele in ls_dp])
    asset_flow = []
    asset_on_date = 0
    for id, money in enumerate(money_flow[::-1]):
        if id == 0:
            asset_on_date = sum_dp
        else:
            asset_on_date -= money_flow[::-1][id-1]
        asset_flow.insert(0, asset_on_date)
    
    # Bagian pembuatan grafik dan file pdf
    def create_graph(fig, y_value, nama, legenda):
        # Pemgambilan value x dan value y
        x = [ele[-5:] for ele in date_list]
        y = y_value
        y_line = 0

        # Pembuatan garis fungsi dan titik nilai
        colors = ['green' if yi > y_line else 'red' for yi in y]

        plt.figure(fig, figsize=(10, 8))
        plt.plot(x, y, color="gray")
        plt.scatter(x, y, color=colors)

        # Pembuatan garis y = 0
        plt.axhline(y=y_line, color='black', linestyle='-')

        # Label-label pada grafik
        plt.xlabel('Tanggal')
        plt.ylabel(legenda)
        plt.xticks(rotation='vertical')
        plt.title(nama)
        plt.grid(True)
        plt.legend([legenda])

        plt.ticklabel_format(style='plain', axis='y')

        # Pembuatan file pdf 
        pdf_file = f'pdf_{fig}.pdf'

        plt.savefig(f'pdf_{fig}.png', dpi=500)

        plt.close(fig)

        c = canvas.Canvas(pdf_file)
        c.setPageSize((800, 600))
        c.drawImage(f'pdf_{fig}.png', 60, 60, width=700, height=500)
        c.save()
    
    # Pembuatan grafik tren pemasukan-pengeluaran
    create_graph(2, money_flow.copy(), "Tren pemasukan-pengeluaran 30 hari terakhir", "Tren pemasukan-pengeluaran")
    # Pembuatan grafik perubahan aset
    create_graph(3, asset_flow.copy(), "Tren perubahan aset 30 hari terakhir", "perubahan aset")

if __name__ == "__main__":
    buat_pdf_2_3()