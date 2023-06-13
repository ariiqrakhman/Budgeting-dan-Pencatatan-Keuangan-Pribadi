import submodules
from datetime import date, timedelta
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors

def buat_pdf_1():
    hd_iv = ["","Tanggal", "Dompet", "Tipe", "pemasukan", "pengeluaran"]
    ls_iv = []

    hd_tr, ls_tr = submodules.open_read_csv("sejarah_transaksi.csv")

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
            ls_iv.append([ id+1, ele[0], ele[3], ele[2], f"Rp{int(ele[4]):>12,}", None ])
        else:
            ls_iv.append([ id+1, ele[0], ele[3], ele[2], None, f"Rp{int(ele[4]):>12,}" ])

    # Generate PDF file
    output_file = "pdf_1.pdf"
    title_text = "Tabel sejarah transaksi 30 hari terakhir"
    doc = SimpleDocTemplate(output_file, pagesize=letter, orientation='portrait')
    elements = []

    # Add the title as a Paragraph object
    styles = getSampleStyleSheet()
    title = Paragraph(title_text, styles['Title'])
    elements.append(title)

    # Convert table data to a list of lists
    table_data = [hd_iv] + ls_iv

    # Create a Table object
    table = Table(table_data)

    # Set the style for the table
    style = TableStyle([
        ('ALIGN', (0, 0), (-1, -1), 'RIGHT'),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.black),  # Set the text color for the header row
        ('BACKGROUND', (0, 0), (-1, 0), colors.grey),  # Set the background color for the header row
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),  # Set the font and style for the header row
        ('FONTSIZE', (0, 0), (-1, 0), 12),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 8),  # Add bottom padding to the header row
        ('TOPPADDING', (0, 0), (-1, 0), 8),  # Add top padding to the header row
        ('BOTTOMPADDING', (0, 1), (-1, -1), 4),  # Add bottom padding to the data rows
        ('TOPPADDING', (0, 1), (-1, -1), 4),  # Add top padding to the data rows
        ('GRID', (0, 0), (-1, -1), 1, colors.black),  # Add borders to all cells
        ('BACKGROUND', (4, 1), (4, -1), colors.lightgreen),  # Set a slightly green background for the fourth column
        ('BACKGROUND', (5, 1), (5, -1), colors.lightcoral),  # Set a slightly red background for the fifth column
    ])
    
    table.setStyle(style)

    # Add the Table object to the elements list
    elements.append(table)

    # Build the PDF document
    doc.build(elements)