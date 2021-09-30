from pathlib import Path
from tkinter import *
from tkinter import filedialog
from PyPDF2 import PdfFileMerger , PdfFileReader

root = Tk()
root.withdraw()

file_selected = filedialog.askopenfile()
input_pathA = Path(file_selected.name)

file_selected = filedialog.askopenfile()
input_pathB = Path(file_selected.name)

DocA = PdfFileReader(str(input_pathA))
DocB = PdfFileReader(str(input_pathB))

MergeAB = PdfFileMerger()
MergeAB.append(str(input_pathA))
MergeAB.append(str(input_pathB))

MergeBA = PdfFileMerger()
MergeBA.append(str(input_pathB))
MergeBA.append(str(input_pathA))

Dir_selected = filedialog.askdirectory()


with Path("AB.pdf").open(mode="wb") as output_file:
    MergeAB.write(output_file)

with Path("BA.pdf").open(mode="wb") as output_file:
    MergeBA.write(output_file)

print("TYPE:") 
print( type(input_pathA))
print("NAME:") 
print(input_pathA.name)
print("OBJECT") 
print(input_pathA)
print(DocA.numPages)

print("TYPE:") 
print( type(input_pathB))
print("NAME:") 
print(input_pathB.name)
print("OBJECT") 
print(input_pathB)
print(DocB.numPages)

