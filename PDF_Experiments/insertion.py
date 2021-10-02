from pathlib import Path
from tkinter import *
from tkinter import filedialog
from PyPDF2 import PdfFileMerger , PdfFileReader, merger

root = Tk()
root.withdraw()

file_selected = filedialog.askopenfile()
input_pathA = Path(file_selected.name)

file_selected = filedialog.askopenfile()
input_pathB = Path(file_selected.name)

Merger = PdfFileMerger()
Merger.append(str(input_pathA))
Merger.merge(1,str(input_pathB))

Dir_selected = filedialog.askdirectory()
print(Dir_selected)
print(type(Dir_selected))
Dir_selected = Dir_selected + "/"

File_Name = input()

with Path(Dir_selected+File_Name+".pdf").open(mode="wb") as output_file:
    Merger.write(output_file)


