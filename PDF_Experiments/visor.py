from tkinter import *
from tkinter import filedialog
from pathlib import Path
from PIL import Image,ImageTk
from pdf2image import convert_from_path


root = Tk()

pdf_frame = Frame(root)
pdf_frame.pack(fill=BOTH,expand=1)

scrol_y = Scrollbar(pdf_frame,orient=VERTICAL)
scrol_x = Scrollbar(pdf_frame,orient=HORIZONTAL)

pdf = Text(pdf_frame,yscrollcommand=scrol_y.set,bg="#525200")
pdf = Text(pdf_frame,xscrollcommand=scrol_x.set,bg="#525200")

scrol_y.pack(side=RIGHT,fill=Y)
scrol_x.pack(side=BOTTOM,fill=X)
scrol_y.config(command=pdf.yview)
scrol_x.config(command=pdf.xview)
pdf.pack(fill=BOTH)

file_selected = filedialog.askopenfile()
input_path = Path(file_selected.name)

pages = convert_from_path(input_path)
photos = []

for i in range(len(pages)):

  print(pages[i].height)
  print(pages[i].width)

  h = pages[i].height
  w = pages[i].width

  TARGET_SIZE = (int(w/6),int(h/6))
  
  resized_img = pages[i].resize(TARGET_SIZE)
  photos.append(ImageTk.PhotoImage(resized_img))

for photo in photos:
  pdf.image_create(END,image=photo)
  pdf.insert(END,'\n\n')
 

mainloop()