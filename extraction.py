from pathlib import Path
from PyPDF2 import PdfFileReader, PdfFileWriter

pdf_path = ( Path.home()/"Desktop"/"pdfmanipulator"/"square.pdf")
input_pdf=PdfFileReader(str(pdf_path))
first_page = input_pdf.getPage(1)
pdf_writer = PdfFileWriter()
pdf_writer.addPage(first_page)
with Path("green_square.pdf").open(mode="wb") as output_file:
    pdf_writer.write(output_file)

