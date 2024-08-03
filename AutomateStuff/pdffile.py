import PyPDF2

pdfFile = open(r'C:\Users\..\Downloads\USCalender.pdf', 'rb')#read binary mode
reader = PyPDF2.PdfReader(pdfFile)
print(len(reader.pages))
print(reader.pages[0])
print(reader.pages[0].extract_text())
for page in range(len(reader.pages)):
    print(reader.pages[page].extract_text())

writer = PyPDF2.PdfWriter()
for page in range(len(reader.pages)):
    pageC = reader.pages[page]
    writer.add_page(pageC)

outputFile = open(r'C:\Users\..\Downloads\copiedPdfUSCalender.pdf', 'wb')
writer.write(outputFile)
outputFile.close()
pdfFile.close()
