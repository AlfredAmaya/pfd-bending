from pathlib import Path
from PyPDF2 import PdfFileReader, pdf

pdf_path = ( Path.home()/"Desktop"/"pdfmanipulator"/"pdfs"/"hello2.pdf")
print("TYPE:") 
print(type(pdf_path))
print("NAME:")
print(pdf_path.name)
print("OBJECT")
print(pdf_path)
document = PdfFileReader(str(pdf_path))

#for page in document.pages:
    #print(page.extractText())
#    print(document.getPageNumber(page))
    
#print( document.documentInfo)
#print(document.numPages)

