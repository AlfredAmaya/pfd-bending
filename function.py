from tkinter import *
from tkinter import filedialog

from pathlib import Path
from PIL import Image,ImageTk
from pdf2image import convert_from_path
import pdf2image
import time
from PyPDF2 import PdfFileReader,PdfFileMerger,PdfFileWriter

file_selected1 = filedialog.askopenfile()
PDF_X = Path(file_selected1.name)

file_selected2 = filedialog.askopenfile()
PDF_Z = Path(file_selected2.name)

folder_selected = filedialog.askdirectory()
PDF_Y = Path(folder_selected)

def getimage (PDF_PATH,DPI,OUTPUT_FOLDER,FIRST_PAGE,LAST_PAGE,FORMAT,USERPWD):
    THREAD_COUNT = 1
    USE_CROPBOX = False
    STRICT = False
    start_time = time.time()
    pil_images = pdf2image.convert_from_path(PDF_PATH, dpi=DPI, output_folder=OUTPUT_FOLDER, first_page=FIRST_PAGE, last_page=LAST_PAGE, fmt=FORMAT, thread_count=THREAD_COUNT, userpw=USERPWD, use_cropbox=USE_CROPBOX, strict=STRICT)
    print ("Time taken : " + str(time.time() - start_time))
    index = 1
    for image in pil_images:
        image.save(str(time.time()) + str(index) + '.'+FORMAT)
        index += 1

 
#getimage(PDF_X,200,PDF_Y,None,None,'jpg',None)

def chain(input_pathA,input_pathB,output_pathC,file_Name):
    fileA = PdfFileReader(str(input_pathA))
    fileB = PdfFileReader(str(input_pathB))
    fileC = PdfFileWriter()
    fileC.appendPagesFromReader(fileA)
    fileC.appendPagesFromReader(fileB)
    output_fileC = Path(output_pathC/file_Name)
    with output_fileC.open(mode="wb") as o_f:
     fileC.write(o_f)

#chain(PDF_Z,PDF_X,PDF_Y,'miarchivo.pdf')

def     