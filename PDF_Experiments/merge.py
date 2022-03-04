from pathlib import Path
from tkinter import *
from tkinter import filedialog
from PyPDF2 import PdfFileMerger , PdfFileWriter

root = Tk()
root.withdraw()

file_selected = filedialog.askopenfile()
input_pathA = Path(file_selected.name)

file_selected = filedialog.askopenfile()
input_pathB = Path(file_selected.name)

MergeAB = PdfFileMerger()
MergeAB.append(str(input_pathA))
MergeAB.append(str(input_pathB))

MergeBA = PdfFileMerger()
MergeBA.append(str(input_pathB))
MergeBA.append(str(input_pathA))

Dir_selected = filedialog.askdirectory()
print(Dir_selected)
print(type(Dir_selected))
Dir_selected = Dir_selected + "/"
print(Dir_selected)
print(type(Dir_selected))

File_Name = input()

with Path(Dir_selected+File_Name+".pdf").open(mode="wb") as output_file:
    PdfFileWriter().addPage(MergeAB.pages[0]).write(output_file)



