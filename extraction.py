from pathlib import Path
from PyPDF2 import PdfFileReader, PdfFileWriter

pdf_path = ( Path.home()/"Desktop"/"pdfmanipulator"/"hello2.pdf")
input_pdf=PdfFileReader(str(pdf_path))
first_page = input_pdf.getPage(0)
pdf_writer = PdfFileWriter()
pdf_writer.addPage(first_page)
