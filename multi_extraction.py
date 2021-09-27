from pathlib import Path

from PyPDF2 import PdfFileReader, PdfFileWriter 

pdf_path = ( Path.home()/"Desktop"/"pdfmanipulator"/"pdfs"/"network_setup_recorder.pdf")
input_pdf = PdfFileReader(str(pdf_path))

pdf_writer = PdfFileWriter()

#for n in range(0, 2):
#    page = input_pdf.getPage(n)
#    page.rotateClockwise(90*n)
#    pdf_writer.addPage(page)

for page in input_pdf.pages[0:4]:
    page.rotateClockwise(90*input_pdf.getPageNumber(page))
    pdf_writer.addPage(page)


with Path("pdfs/chapter1slice.pdf").open(mode="wb") as output_file:
    pdf_writer.write(output_file)



