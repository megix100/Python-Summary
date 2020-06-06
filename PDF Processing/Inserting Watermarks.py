# import os
# import PyPDF2
#
# path="D:\\CIRO (Estudos Compactados)\\CENTENNIAL\\CENTENNIAL (ENERGY ENGINEERING)\\Matérias\\Python\\Projects\\PDF Processing\\Watermark"
# input_watermark = PyPDF2.PdfFileReader(open("watermark.pdf", "rb"))
# watermark_page = input_watermark.getPage(0)
# output = PyPDF2.PdfFileWriter()
# os.chdir(path)
# for filename in os.listdir(path):  #Checking each file inside the folder
#     input_file=PyPDF2.PdfFileReader(open(f"{filename}", "rb"))
#     for i in range(input_file.numPages):  #Checking each page inside the file
#         page=input_file.getPage(i)
#         page.mergePage(watermark_page)
#         output.addPage(page)
#         with open(f"{filename}", "wb") as outputStream:
#             output.write(outputStream)

import os
import PyPDF2

path="D:\CIRO (Estudos Compactados)\CENTENNIAL\CENTENNIAL (ENERGY ENGINEERING)\Matérias\Python\Projects\PDF Processing\Watermark"
watermark = PyPDF2.PdfFileReader(open('watermark.pdf', 'rb'))
os.chdir(path)
template = PyPDF2.PdfFileReader(open('fw9.pdf', 'rb'))
output = PyPDF2.PdfFileWriter()
for i in range(template.getNumPages()): #Checking each page inside the file
    page = template.getPage(i)
    page.mergePage(watermark.getPage(0))
    output.addPage(page)

    with open('watermarked_output.pdf', 'wb') as file:
        output.write(file)