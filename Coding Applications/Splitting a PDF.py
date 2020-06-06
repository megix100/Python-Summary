import os
import PyPDF2
#--------Test
path="D:\CIRO (Estudos Compactados)\CENTENNIAL\CENTENNIAL (ENERGY ENGINEERING)\Matérias\Python\Projects\PDF Processing\PDF Processing"
os.chdir(path)
inputpdf = PyPDF2.PdfFileReader(open("fw9.pdf", "rb"))
for i in range(inputpdf.numPages):
    output = PyPDF2.PdfFileWriter()
    output.addPage(inputpdf.getPage(i))
    with open("document-page%s.pdf" % i, "wb") as outputStream:
        output.write(outputStream)