import PyPDF2
with open("dummy.pdf","rb") as file: #You have to put rb because the PDF document is read in binary
	print(file)
	reader=PyPDF2.PdfFileReader(file)
	print(reader.numPages)
	print(reader.getPage(0)) #Get the Page object
	page=reader.getPage(0)#Get the Page object
	page.rotateClockwise(90)#It just works if the Page was selected using getPage
	writer=PyPDF2.PdfFileWriter() #Enables the Writing Mode
	writer.addPage(page)#Put a new page wth the modifications above
	#Even after appearing that you rotate the file, everything is in the memory, you need to save it to apply it
	with open("tilt.pdf","wb") as new_file:#Remember always binary
	#Create another file "tilt.pdf" with the modifications
		writer.write(new_file) #Save the document


