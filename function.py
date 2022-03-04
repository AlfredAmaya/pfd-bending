from tkinter import *
from tkinter import filedialog

from pathlib import Path
from PIL import Image,ImageTk
from pdf2image import convert_from_path
import pdf2image
import time
from PyPDF2 import PdfFileReader,PdfFileMerger,PdfFileWriter
from os import remove

file_selected1 = filedialog.askopenfile()
PDF_X = Path(file_selected1.name)

file_selected2 = filedialog.askopenfile()
PDF_Z = Path(file_selected2.name)

folder_selected = filedialog.askdirectory()
PDF_Y = Path(folder_selected)

def getALLimages (PDF_PATH,DPI,OUTPUT_FOLDER,FIRST_PAGE,LAST_PAGE,FORMAT,USERPWD):
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

chain(PDF_X,PDF_Z,PDF_Y,'unchain.pdf')

def extract(input_path,output_path,start,end,file_name):
    input_file = PdfFileReader(str(input_path))
    output_file = PdfFileWriter()
    if end==None or end==start:
        only_page=input_file.getPage(start-1)
        output_file.addPage(only_page)
    else:
        for page in input_file.pages[start-1:end]:
            output_file.addPage(page)

    final_file_output = Path(output_path/file_name)
    with final_file_output.open(mode="wb") as o_f:
        output_file.write(o_f)

#extract(PDF_X,PDF_Y,2,None,'extractionfile.pdf')

def merger(input_pathA,input_pathB,output_pathC,before_page,start,end,file_name):
    input_fileA = PdfFileReader(str(input_pathA))
    input_fileB = PdfFileReader(str(input_pathB))
    output_file = PdfFileMerger()
    output_file.append(str(input_pathA))
    proxy = PdfFileWriter()
    
    if end==None or end==start: 
        proxy.addPage(input_fileB.getPage(start-1))
    else:
        for page in input_fileB.pages[start-1:end]:
           proxy.addPage(page)

    cache_path = Path(output_pathC/'proxy_cache.pdf')
    with cache_path.open(mode="wb") as c_f:
        proxy.write(c_f)
    
    output_file.merge(before_page,str(cache_path))

    final_file_output_path = Path(output_pathC/file_name)
    with final_file_output_path.open(mode="wb") as o_f:
        output_file.write(o_f)

#merger(PDF_X,PDF_Z,PDF_Y,3,1,2,'inception2.pdf')

def mix(input_pathA,input_pathB,output_pathC,file_name):
    input_fileA = PdfFileReader(str(input_pathA))
    max_pageA = len(input_fileA.pages)+1

    input_fileB = PdfFileReader(str(input_pathB))
    max_pageB = len(input_fileB.pages)+1

    output_file = PdfFileMerger()

    output_file.append(str(input_pathA))

    cache_path = Path(output_pathC/'proxy_mix_cache.pdf')

    if (len(input_fileA.pages) >= len(input_fileB.pages)):
        for page in input_fileB.pages:
            # Extraer hojas en un archivo proxy------------------------------------------------------------------
            proxy = PdfFileWriter()
            proxy.addPage(page)
            with cache_path.open(mode="wb") as c_f:
                proxy.write(c_f)
                
            
            #Dcidir donde debe ir--------------------------------------------------------------------------------
            num_page = (input_fileB.getPageNumber(page)) + 1
            after_page = (num_page*2)-1
            #Insertar--------------------------------------------------------------------------------------------
            output_file.merge(after_page,str(cache_path))

    elif len(input_fileA.pages) > len(input_fileB.pages):
        # Extraer hojas en un archivo proxy----------------------------------------------------------------------
        A_bottom = (len(input_fileA.pages)*2)- 1
        B_actual = 1
        a_p = 1
        for page in input_fileB.pages:
            proxy = PdfFileWriter()
            proxy.addPage(page)
            with cache_path.open(mode="wb") as c_f:
                proxy.pages.write(c_f)
                
            
        #Determinar en que pagina debe ir-------------------------------------------------------------------------
            num_page = (input_fileB.getPageNumber(page)) + 1
            if A_bottom > a_p:
                B_actual = num_page*2
                a_p = B_actual - 1
                output_file.merge(a_p,str(cache_path))
                
            else:
                a_p = B_actual
                B_actual = B_actual + 1
                output_file.merge(a_p,str(cache_path))
    print(len(output_file.pages))
    final_file_output_path = Path(output_pathC/file_name)
    with final_file_output_path.open(mode="wb") as o_f:
        output_file.write(o_f)     
                



 

