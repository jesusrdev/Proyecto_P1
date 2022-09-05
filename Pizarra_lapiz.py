from tkinter import *
from calculator import open_calculator
from PIL import ImageTk, Image
from Funcion_buscador import open_browser
from tkinter.ttk import Notebook
from tkinter.colorchooser import askcolor
import time
import pyautogui

ventana=Tk()    
ventana.state('zoomed')
ventana.title("Pizarra Virtual")
# ventana.geometry('1000x500')

menu_ventanas = Notebook(ventana)
menu_ventanas.grid(row = 0, column = 0)
altura_pantalla = ventana.winfo_screenheight()
ancho_pantalla = ventana.winfo_screenwidth() - int(500)
#--------------CONTADOR----------------
contador_new_window = 1

#-------------IMAGENES--------------------
imagen_lapiz = PhotoImage(file = r'./iconos/icono-pen.png')

icono_tools_calculadora = PhotoImage(file = r'./iconos/icono-calculadora-tools.png')
icono_tools_internet = PhotoImage(file = r'./iconos/icono-internet-tools.png')
icono_tools_recortar = PhotoImage(file = r'./iconos/icono-recortar-tools.png')
icono_tools_capturar_pantalla = PhotoImage(file = r'./iconos/icono-capturar-todo.png')

icono_window_newwindow = PhotoImage(file = r'./iconos/icono-window.png')
icono_window_delete = PhotoImage(file = r'./iconos/icono-remove-window.png')

frame_1 = Frame(menu_ventanas, width = 1500, height = 1500 )


#-------------FUNCIONES DE WINDOW-----------------


def funcion_crear_ventanas():
    global contador_new_window
    contador_new_window = contador_new_window + 1
    name = 'ventana' + str(contador_new_window)
    for i in range (contador_new_window):
        if i == (contador_new_window-1):
            frame_x = 'frame' + str(contador_new_window)
            frame_x = Frame(menu_ventanas, width = 1500, height = 1500 )
            
            frame_principal = Frame (frame_x, height = 500, width = 500 )
            frame_principal.grid(row =1, column = 0 )

            etiqueta_opciones=Label(frame_principal)
            etiqueta_opciones.grid(row = 1)

            global framecanva
            framecanva = Frame(frame_principal, height = altura_pantalla, width = ancho_pantalla)
            framecanva.grid(row = 1, rowspan = 3, column = 1)

            class Paint(object):

                DEFAULT_PEN_SIZE = 5.0
                DEFAULT_COLOR = 'black'
            #
                DEFAULT_TEXT = 'Helvetica 15 bold'
            #
                def __init__(self):
                    self.boton_recortar = Button(framecanva, image = icono_tools_recortar, borderwidth = 0, command = self.recortador_pantalla )
                    self.boton_recortar.grid(column = 7, row = 0)

                    self.boton_recortar_todo = Button(framecanva, image = icono_tools_capturar_pantalla, borderwidth = 0, command = self.take_screenshot)
                    self.boton_recortar_todo.grid(column = 6, row = 0)
                    
                    self.pen_logo = ImageTk.PhotoImage(Image.open(r'./iconos/icono-pen.png'))
                    self.pen_button = Button(framecanva,padx=6,image=self.pen_logo,borderwidth=2, command=self.use_pen)
                    self.pen_button.grid(column = 1, row = 0)

                    self.color_logo = ImageTk.PhotoImage(Image.open(r'./iconos/icono-colores.png'))
                    self.color_button = Button(framecanva,image = self.color_logo,borderwidth=2, command=self.choose_color)
                    self.color_button.grid(column = 2, row = 0)

                    self.eraser_logo = ImageTk.PhotoImage(Image.open(r'./iconos/icono-eraser.png'))
                    self.eraser_button = Button(framecanva,image = self.eraser_logo,borderwidth=2, command=self.use_eraser)
                    self.eraser_button.grid(column = 3, row = 0)

                    self.pen_size = Label(framecanva,text="Pen Size",font=('verdana',10,'bold'))
                    self.pen_size.grid(column = 4, row = 0)
                    self.choose_size_button = Scale(framecanva, from_=1, to=20, orient = HORIZONTAL)
                    self.choose_size_button.grid(column = 5, row = 0)
                    
                    self.vp_button = Button(framecanva, image = icono_window_newwindow, borderwidth=2, command = funcion_crear_ventanas)
                    self.vp_button.grid(column = 8, row = 0)

                    self.boton_delete_window = Button(framecanva, image = icono_window_delete, borderwidth = 0, command = lambda: menu_ventanas.forget(frame_x))
                    self.boton_delete_window.grid(column = 9, row = 0)

                    self.boton_calculadora = Button(framecanva, image = icono_tools_calculadora,command = open_calculator, borderwidth = 0)
                    self.boton_calculadora.grid(column = 10, row = 0)

                    self.boton_internet = Button(framecanva, image = icono_tools_internet, command = open_browser ,borderwidth = 0)
                    self.boton_internet.grid(column = 11, row = 0)

                    self.altura_pantalla = ventana.winfo_screenheight()
                    self.ancho_pantalla = ventana.winfo_screenwidth()
                    self.c = Canvas(frame_x, bg='white', width = self.ancho_pantalla, height= self.altura_pantalla, relief=RIDGE,borderwidth=0)
                    self.c.grid(row = 4, column = 0, columnspan = 5 )

                    self.setup()

                    

                def setup(self):
                    self.old_x = None
                    self.old_y = None
                    self.line_width = self.choose_size_button.get()
                    self.color = self.DEFAULT_COLOR
                    self.texto = self.DEFAULT_TEXT
                    self.eraser_on = False
                    self.active_button = self.pen_button
                    self.c.bind('<B1-Motion>', self.paint)
                    self.c.bind('<ButtonRelease-1>', self.reset)

                def recortador_pantalla(self):
                    ventana.iconify()

                    global coordenadas
                    coordenadas = []
                    def get_event(event):
                        if len(coordenadas) <= 2:
                            coordenadas.append(event.x)
                            coordenadas.append(event.y)

                        else:
                            self.ventana_transparente.withdraw()
                            coordenadas[2] -= coordenadas[0]
                            coordenadas[3] -= coordenadas[1]
                            self.tupla = tuple(coordenadas)

                            self.im1 = pyautogui.screenshot(region=self.tupla)

                            self.im1 = ImageTk.PhotoImage(self.im1)

                            self.c.create_image(0, 0, image = self.im1, anchor=NW)       

                            coordenadas.clear()
                            ventana.deiconify()
                    

                    # Ventana Transparente
                    self.ventana_transparente = Toplevel()
                    self.ventana_transparente.attributes('-alpha',0.1)
                    self.ventana_transparente.attributes('-fullscreen', True)
                    self.ventana_transparente.bind("<Button-1>", get_event)

                # Define a function to take the screenshot
                def take_screenshot(self):
                    ventana.iconify()
                    time.sleep(0.5)
                    altura_pantalla = ventana.winfo_screenheight()
                    ancho_pantalla = ventana.winfo_screenwidth()
                    self.im1 = pyautogui.screenshot(region = (0,0,ancho_pantalla,altura_pantalla))

                    # Abrir nueva ventana con la imagen
                    self.im1 = ImageTk.PhotoImage(self.im1)

                    self.c.create_image(0, 0, image =self.im1, anchor=NW)     

                    ventana.deiconify()


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
                
                    
                def reset(self, event):
                    self.old_x, self.old_y = None, None

            if __name__ == '__main__':
                Paint()
            paint = Paint()
            menu_ventanas.add(frame_x, text = name)



#-----------------BOTONES---------------
frame_principal = Frame (frame_1, height = 500, width = 500 )
frame_principal.grid(row =1, column = 0 )

etiqueta_opciones=Label(frame_principal)
etiqueta_opciones.grid(row = 1)


global framecanva
framecanva = Frame(frame_principal, height = altura_pantalla, width = ancho_pantalla)
framecanva.grid(row = 1, rowspan = 3, column = 1)
#----------------PIZARRA------------------------
class Paint(object):

    DEFAULT_PEN_SIZE = 5.0
    DEFAULT_COLOR = 'black'
#
    DEFAULT_TEXT = 'Helvetica 15 bold'
#
    def __init__(self):
#-------------------------
        self.boton_recortar = Button(framecanva, image = icono_tools_recortar, borderwidth = 0, command = self.recortador_pantalla )
        self.boton_recortar.grid(column = 7, row = 0)

        self.boton_recortar_todo = Button(framecanva, image = icono_tools_capturar_pantalla, borderwidth = 0, command = self.take_screenshot)
        self.boton_recortar_todo.grid(column = 6, row = 0)
        
        self.pen_logo = ImageTk.PhotoImage(Image.open(r'./iconos/icono-pen.png'))
        self.pen_button = Button(framecanva,padx=6,image=self.pen_logo,borderwidth=2, command=self.use_pen)
        self.pen_button.grid(column = 1, row = 0)

        self.color_logo = ImageTk.PhotoImage(Image.open(r'./iconos/icono-colores.png'))
        self.color_button = Button(framecanva,image = self.color_logo,borderwidth=2, command=self.choose_color)
        self.color_button.grid(column = 2, row = 0)

        self.eraser_logo = ImageTk.PhotoImage(Image.open(r'./iconos/icono-eraser.png'))
        self.eraser_button = Button(framecanva,image = self.eraser_logo,borderwidth=2, command=self.use_eraser)
        self.eraser_button.grid(column = 3, row = 0)

        self.pen_size = Label(framecanva,text="Pen Size",font=('verdana',10,'bold'))
        self.pen_size.grid(column = 4, row = 0)
        self.choose_size_button = Scale(framecanva, from_=1, to=20, orient = HORIZONTAL)
        self.choose_size_button.grid(column = 5, row = 0)
        
        self.vp_button = Button(framecanva, image = icono_window_newwindow, borderwidth=2, command = funcion_crear_ventanas)
        self.vp_button.grid(column = 8, row = 0)

        self.boton_delete_window = Button(framecanva, image = icono_window_delete, borderwidth = 0, command = lambda: menu_ventanas.forget(frame_1))
        self.boton_delete_window.grid(column = 9, row = 0)

        self.boton_calculadora = Button(framecanva, image = icono_tools_calculadora,command = open_calculator, borderwidth = 0)
        self.boton_calculadora.grid(column = 10, row = 0)

        self.boton_internet = Button(framecanva, image = icono_tools_internet, command = open_browser ,borderwidth = 0)
        self.boton_internet.grid(column = 11, row = 0)

        self.altura_pantalla = ventana.winfo_screenheight()
        self.ancho_pantalla = ventana.winfo_screenwidth()
        self.c = Canvas(frame_1, bg='white', width = self.ancho_pantalla, height= self.altura_pantalla, relief=RIDGE,borderwidth=0)
        self.c.grid(row = 4, column = 0, columnspan = 5 )

        self.setup()


    def setup(self):
        self.old_x = None
        self.old_y = None
        self.line_width = self.choose_size_button.get()
        self.color = self.DEFAULT_COLOR
        self.texto = self.DEFAULT_TEXT
        self.eraser_on = False
        self.active_button = self.pen_button
        self.c.bind('<B1-Motion>', self.paint)
        self.c.bind('<ButtonRelease-1>', self.reset)
        # self.ventana_transparente.bind("<Button-1>", self.get_event)

    def recortador_pantalla(self):
        ventana.iconify()

        global coordenadas
        coordenadas = []
        def get_event(event):
            if len(coordenadas) <= 2:
                coordenadas.append(event.x)
                coordenadas.append(event.y)
                # print(coordenadas)
            else:
                self.ventana_transparente.withdraw()
                coordenadas[2] -= coordenadas[0]
                coordenadas[3] -= coordenadas[1]
                self.tupla = tuple(coordenadas)
                # print(tupla)

                self.im1 = pyautogui.screenshot(region=self.tupla)

                self.im1 = ImageTk.PhotoImage(self.im1)

                self.c.create_image(0, 0, image = self.im1, anchor=NW)       

                coordenadas.clear()
                ventana.deiconify()
        

        # Ventana Transparente
        self.ventana_transparente = Toplevel()
        self.ventana_transparente.attributes('-alpha',0.1)
        self.ventana_transparente.attributes('-fullscreen', True)
        self.ventana_transparente.bind("<Button-1>", get_event)

    # Define a function to take the screenshot
    def take_screenshot(self):
        ventana.iconify()
        time.sleep(0.5)
        altura_pantalla = ventana.winfo_screenheight()
        ancho_pantalla = ventana.winfo_screenwidth()
        self.im1 = pyautogui.screenshot(region = (0,0,ancho_pantalla,altura_pantalla))

        # Abrir nueva ventana con la imagen
        self.im1 = ImageTk.PhotoImage(self.im1)

        self.c.create_image(0, 0, image =self.im1, anchor=NW)     

        ventana.deiconify()


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
    
        
    def reset(self, event):
        self.old_x, self.old_y = None, None

if __name__ == '__main__':
    Paint()
paint = Paint()
#----------------------------------------------
menu_ventanas.add(frame_1, text = "Ventana")

ventana.mainloop()