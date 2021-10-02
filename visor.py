# Importing required modules
from tkinter import *
from PIL import Image,ImageTk
from pdf2image import convert_from_path

# Creating Tk container
root = Tk()
# Creating the frame for PDF Viewer
pdf_frame = Frame(root).pack(fill=BOTH,expand=1)
# Adding Scrollbar to the PDF frame
scrol_y = Scrollbar(pdf_frame,orient=VERTICAL)
scrol_x = Scrollbar(pdf_frame,orient=HORIZONTAL)
# Adding text widget for inserting images
# Setting the scrollbar to the right side
pdf = Text(pdf_frame,yscrollcommand=scrol_y.set,bg="grey")
pdf = Text(pdf_frame,xscrollcommand=scrol_x.set,bg="grey")
scrol_y.pack(side=RIGHT,fill=Y)
scrol_x.pack(side=BOTTOM,fill=X)
scrol_y.config(command=pdf.yview)
scrol_x.config(command=pdf.xview)


# Finally packing the text widget
pdf.pack(fill=BOTH,expand=10)
# Here the PDF is converted to list of images
pages = convert_from_path('pdfs/hello2+square.pdf')
# Empty list for storing images
photos = []
# Storing the converted images into list
for i in range(len(pages)):
  photos.append(ImageTk.PhotoImage(pages[i]))
# Adding all the images to the text widget
for photo in photos:
  pdf.image_create(END,image=photo)
  
  # For Seperating the pages
  pdf.insert(END,'\n\n')
# Ending of mainloop
mainloop()