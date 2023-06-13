import matplotlib.pyplot as plt
from reportlab.pdfgen import canvas
import datetime
import submodules

def buat_pdf_2():
    # Get today's date
    current_date = datetime.date.today()

    # Create a list to store the dates
    date_list = []

    for i in range(30, -1, -1):
        date = current_date - datetime.timedelta(days=i)
        date_list.append(date.strftime("%Y/%m/%d"))

    hd_tr, ls_tr = submodules.open_read_csv("sejarah_transaksi.csv")
    money_flow = []
    i = 0
    for date in (date_list):
        money_flow_on_date = 0
        for baris in ls_tr:
            date_str, kode, tipe, dompet, nominal = baris
            kode, nominal = int(kode), int(nominal)
            if date == date_str:
                money_flow_on_date = money_flow_on_date + nominal if kode == 1 else money_flow_on_date - nominal
            elif date > date_str:
                break
        money_flow.append(money_flow_on_date)

    x = [ele[-5:] for ele in date_list]
    y = money_flow.copy()
    y_line = 0

    colors = ['green' if yi > y_line else 'red' for yi in y]

    # Plotting the line and points with colors
    plt.figure(2)
    plt.plot(x, y, color="gray")
    plt.scatter(x, y, color=colors)

    plt.axhline(y=y_line, color='black', linestyle='-')

    plt.xlabel('Tanggal')
    plt.ylabel('Perubahan uang')
    plt.xticks(rotation='vertical')
    plt.title('Grafik keuangan dalam 1 bulan')
    plt.grid(True)
    plt.legend(['Perubahan uang'])

    # Save the plot as a PDF using reportlab
    pdf_file = 'pdf_2.pdf'

    # Adjust the dpi value to increase the resolution of the saved image
    plt.savefig('pdf_2.png', dpi=500)  # Save the chart as an image

    # Create a PDF canvas
    c = canvas.Canvas(pdf_file)
    c.setPageSize((800, 600))  # Set the PDF page size to match the chart size
    c.drawImage('pdf_2.png', 60, 60, width=640, height=440)  # Add the chart image to the PDF
    c.save()
