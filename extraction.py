from pathlib import Path
from PyPDF2 import PdfFileReader, PdfFileWriter

pdf_path = ( Path.home()/"Desktop"/"pdfmanipulator"/"hello2.pdf")
input_pdf=PdfFileReader(str(pdf_path))
