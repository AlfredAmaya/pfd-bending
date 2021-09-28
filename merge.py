from PyPDF2 import PdfFileMerger
from pathlib import Path

from tkinter import filedialog
from tkinter import *

pdf_merger = PdfFileMerger()

root = Tk()
root.withdraw()
folder_selected = filedialog.askdirectory()

input_path = Path(folder_selected)

for path in input_path.glob("*.pdf"):
    print(path.name)

expense_reports = list(input_path.glob("*.pdf"))
expense_reports.sort()

