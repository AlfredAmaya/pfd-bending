from pathlib import Path
from PyPDF2 import PdfFileReader, PdfFileWriter 

pdf_path = ( Path.home()/"Desktop"/"pdfmanipulator"/"pdfs"/"square.pdf")
squares_pdf = PdfFileReader(str(pdf_path))
pdf_path = ( Path.home()/"Desktop"/"pdfmanipulator"/"pdfs"/"hello2.pdf")
hello2_pdf = PdfFileReader(str(pdf_path))

target_writer = PdfFileWriter()
target_writer.appendPagesFromReader(hello2_pdf)
target_writer.appendPagesFromReader(squares_pdf)

with Path("pdfs/hello2+square.pdf").open(mode="wb") as output_file:
     target_writer.write(output_file)
