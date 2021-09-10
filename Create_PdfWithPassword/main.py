#pip install PyPDF2
from PyPDF2 import PdfFileWriter,PdfFileReader

def secure_pdf(file,password):
    p = PdfFileWriter()
    pdf=PdfFileReader(file)
    for i in range(pdf.numPages):
        p.addPage(pdf.getPage(i))
    p.encrypt(password)
    with open(f"encrypted_{file}","wb") as f:
        p.write(f)
        f.close()
    print(f"encrypted_{file}Created....")

if __name__ == "__main__":
    file="Your pdf file name.pdf"
    password = "give password here"
    secure_pdf(file,password)
    
    
