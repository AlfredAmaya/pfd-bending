from pathlib import Path
from PyPDF2 import PdfFileReader
from reportlab.pdfbase.pdfdoc import Pages

pdf_path = ( Path.home()/"Desktop"/"pdfmanipulator"/"hello2.pdf")

document = PdfFileReader(str(pdf_path))
document.getNumPages()

for page in document.pages:
    print(page.extractText())
    print(document.getPageNumber(page))
    
print( document.documentInfo)
print(document.numPages)

