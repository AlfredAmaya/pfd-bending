from PyPDF2 import PdfFileReader, PdfFileWriter
from pathlib import Path

pdf_path = ( Path.home()/"Desktop"/"pdfmanipulator"/"network_setup_recorde.pdf")
input_pdf = PdfFileReader(str(pdf_path))

pdf_writer = PdfFileWriter()
pdf_writer_2 = PdfFileWriter()
for n in range(0, 2):
    page = input_pdf.getPage(n)
    pdf_writer.addPage(page)

with Path("chapter1.pdf").open(mode="wb") as output_file:
    pdf_writer.write(output_file)



