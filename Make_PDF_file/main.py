# pip install fpdf

from fpdf import FPDF
pdf = FPDF()
pdf.add_page()
pdf.set_font("Arial",size=15)

pdf.cell(200,10,txt="Tkinter in Python. .",ln=1,align='C')
pdf.cell(20,10,txt="Tkinter is the most commonly used library for developing GUI  in Python .", ln=1 , align='L',fill=False)

# put the name of pdf
pdf.output("tkinter.pdf")
