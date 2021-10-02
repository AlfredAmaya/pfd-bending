from reportlab.pdfgen import canvas
from reportlab.lib.units import inch, cm
def hello(c):
    c.line(100,100,200,100)
    c.line(200,100,200,200)
    c.line(200,200,100,200)
    c.line(100,200,100,100)

c = canvas.Canvas("square.pdf",pagesize=(8.5 * inch, 11 * inch))

hello(c)
c.showPage()

c.setStrokeColorRGB(0.2,0.5,0.3)
hello(c)
c.showPage()

c.setStrokeColorRGB(0.5,0.3,0.2)
hello(c)
c.showPage()

c.save()