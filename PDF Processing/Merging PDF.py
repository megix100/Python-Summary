import PyPDF2
import os

#Using a Folder with all the PDFs to be merged
def mergepdf(path):
    os.chdir(path)
    merger=PyPDF2.PdfFileMerger()
    for filename in os.listdir(path): #Checking each file inside the folder
        merger.append(filename)
    merger.write("NewPDF.pdf")
mergepdf("D:\CIRO (Estudos Compactados)\CENTENNIAL\CENTENNIAL (ENERGY ENGINEERING)\Matérias\Python\Projects\PDF Processing\PDF Processing")

#Using the Name of the PDFs to be merged
path="D:\CIRO (Estudos Compactados)\CENTENNIAL\CENTENNIAL (ENERGY ENGINEERING)\Matérias\Python\Projects\PDF Processing\PDF Processing"
def mergepdf(*files):
    os.chdir(path)
    merger=PyPDF2.PdfFileMerger()
    for filename in files:
        merger.append(filename)
    merger.write("NewPDFbyname.pdf")
mergepdf("dummy.pdf","twopage.pdf" )