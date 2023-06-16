from . import submodules as sdl
from datetime import date, timedelta
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors

def buat_pdf_1():
    hd_iv = ["","Tanggal", "Dompet", "Tipe", "pemasukan", "pengeluaran"]
    ls_iv = []

    _, ls_tr = sdl.open_read_csv("sejarah_transaksi.csv")

    # Restriksi 30 hari yg lalu
    hari_ini = date.today()
    hari_30_belakang = (hari_ini - timedelta(days=30)).strftime("%Y/%m/%d")
    ls_tr_new = []
    for ele in ls_tr:
        if ele[0] < hari_30_belakang:
            break
        ls_tr_new.append(ele)

    # Pembuatan baris invoice pertabel
    for id,ele in enumerate(ls_tr_new):
        if ele[1] == "1":
            ls_iv.append([ id+1, ele[0], ele[3], ele[2], f"Rp{int(ele[4]):>10,}", None ])
        else:
            ls_iv.append([ id+1, ele[0], ele[3], ele[2], None, f"Rp{int(ele[4]):>10,}" ])

    # Pembuatan file pdf
    output_file = "pdf_1.pdf"
    title_text = "Tabel sejarah transaksi 30 hari terakhir"
    doc = SimpleDocTemplate(output_file, pagesize=letter, orientation='portrait')
    elements = []

    # Penambahan judul pada file
    styles = getSampleStyleSheet()
    title = Paragraph(title_text, styles['Title'])
    elements.append(title)

    # Mengumpulkan data tabel terdiri dari header dan isi
    table_data = [hd_iv] + ls_iv

    # Membuat objek/memori tabel
    table = Table(table_data)

    # Membuat model tabel
    style = TableStyle([
        ('ALIGN', (0, 0), (-1, -1), 'RIGHT'),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.black),  # Setting font color header
        ('BACKGROUND', (0, 0), (-1, 0), colors.grey),  # Setting backgroung header
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),  # Setting font style header
        ('FONTSIZE', (0, 0), (-1, 0), 12),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 8), 
        ('TOPPADDING', (0, 0), (-1, 0), 8),  
        ('BOTTOMPADDING', (0, 1), (-1, -1), 4),  
        ('TOPPADDING', (0, 1), (-1, -1), 4),  
        ('GRID', (0, 0), (-1, -1), 1, colors.black),  # Setting cell border
        ('BACKGROUND', (4, 1), (4, -1), colors.lightgreen),  # Setting background hijau kolom ke-4
        ('BACKGROUND', (5, 1), (5, -1), colors.lightcoral),  # Setting backgroung merah kolom ke-5
    ])
    
    table.setStyle(style)

    # Tambahkan tabel
    elements.append(table)

    # Buat file pdf
    doc.build(elements)