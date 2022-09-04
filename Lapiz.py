from tkinter import *
from tkinter.colorchooser import askcolor
from PIL import ImageTk, Image 

class Paint(object):
 
    DEFAULT_PEN_SIZE = 5.0
    DEFAULT_COLOR = 'black'
 
    def __init__(self):
        self.ventana_lapiz = Toplevel()
        self.ventana_lapiz.title("Pizarra")
       
        self.paint_tools = Frame(self.ventana_lapiz,width=500,height=500,relief=RIDGE,borderwidth=2, bg = 'white')

        self.paint_tools.grid(column = 0, row = 0)
 
        self.pen_logo = ImageTk.PhotoImage(Image.open(r'./iconos/icono-pen.png'))
        self.p = Label(self.paint_tools, text="pen",borderwidth=0,font=('verdana',10,'bold'))
        self.p.grid(column = 0, row = 1)
        self.pen_button = Button(self.paint_tools,padx=6,image=self.pen_logo,borderwidth=2,command=self.use_pen)
        self.pen_button.grid(column = 1, row = 1)
 
        self.brush_logo = ImageTk.PhotoImage(Image.open(r'./iconos/icono-borrar-edit.png'))
        self.b = Label(self.paint_tools,borderwidth=0,text='brush',font=('verdana',10,'bold'))
        self.b.grid(column = 0, row = 2)
        self.brush_button = Button(self.paint_tools,image = self.brush_logo,borderwidth=2,command=self.use_brush)
        self.brush_button.grid(column = 1, row = 2)
 
        self.color_logo = ImageTk.PhotoImage(Image.open(r'./iconos/icono-colores.png'))
        self.cl = Label(self.paint_tools, text='color',font=('verdana',10,'bold'))
        self.cl.grid(column = 0, row = 3)
        self.color_button = Button(self.paint_tools,image = self.color_logo,borderwidth=2,command=self.choose_color)
        self.color_button.grid(column = 1, row = 3)
 
        self.eraser_logo = ImageTk.PhotoImage(Image.open(r'./iconos/icono-eraser.png'))
        self.e = Label(self.paint_tools, text='eraser',font=('verdana',10,'bold'))
        self.e.grid(column = 0, row = 4)
        self.eraser_button = Button(self.paint_tools,image = self.eraser_logo,borderwidth=2,command=self.use_eraser)
        self.eraser_button.grid(column = 1, row = 4)
 
        self.pen_size = Label(self.paint_tools,text="Pen Size",font=('verdana',10,'bold'))
        self.pen_size.grid(column = 0, row = 5)
        self.choose_size_button = Scale(self.paint_tools, from_=1, to=20, orient=VERTICAL)
        self.choose_size_button.grid(column = 1, row = 5)
        
        self.ventanaprincipal_logo = ImageTk.PhotoImage(Image.open(r'./iconos/return_ventana.png'))
        self.ventanaprincipal = Label(self.paint_tools, text='Window',font=('verdana',10,'bold'))
        self.ventanaprincipal.grid(column = 0, row = 6)
        self.vp_button = Button(self.paint_tools, image = self.ventanaprincipal_logo,borderwidth=2,command=self.return_window )
        self.vp_button.grid(column = 1, row = 6)
 
        altura_pantalla = self.ventana_lapiz.winfo_screenheight()
        ancho_pantalla = self.ventana_lapiz.winfo_screenwidth() - int(100)
        self.c = Canvas(self.ventana_lapiz, bg='white', width = ancho_pantalla, height=altura_pantalla,relief=RIDGE,borderwidth=0)
        self.c.grid(row = 0, column = 2)
 
        self.setup()
        self.ventana_lapiz.mainloop()

    def setup(self):
        self.old_x = None
        self.old_y = None
        self.line_width = self.choose_size_button.get()
        self.color = self.DEFAULT_COLOR
        self.eraser_on = False
        self.active_button = self.pen_button
        self.c.bind('<B1-Motion>', self.paint)
        self.c.bind('<ButtonRelease-1>', self.reset)
 
    def use_pen(self):
        self.activate_button(self.pen_button)
 
    def use_brush(self):
        self.activate_button(self.brush_button)
 
    def choose_color(self):
        self.eraser_on = False
        self.color = askcolor(color=self.color)[1]
 
    def use_eraser(self):
        self.activate_button(self.eraser_button, eraser_mode=True)
 
    def activate_button(self, some_button, eraser_mode=False):
        self.active_button.config(relief=RAISED)
        some_button.config(relief=SUNKEN)
        self.active_button = some_button
        self.eraser_on = eraser_mode
 
    def paint(self, event):
        self.line_width = self.choose_size_button.get()
        paint_color = 'white' if self.eraser_on else self.color
        if self.old_x and self.old_y:
            self.c.create_line(self.old_x, self.old_y, event.x, event.y,
                               width=self.line_width, fill=paint_color,
                               capstyle=ROUND, smooth=TRUE, splinesteps=36)
        self.old_x = event.x
        self.old_y = event.y
#
    def return_window(self):
        self.ventana_lapiz.withdraw()
      
        
    def reset(self, event):
        self.old_x, self.old_y = None, None
