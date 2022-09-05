from tkinter import *
import pyautogui
from PIL import ImageTk
import time

def recortador_pantalla(ventana,my_canvas):
    ventana.iconify()

    global coordenadas
    coordenadas = []
    def get_event(event):
        if len(coordenadas) <= 2:
            coordenadas.append(event.x)
            coordenadas.append(event.y)
            # print(coordenadas)
        else:
            ventana_transparente.withdraw()
            coordenadas[2] -= coordenadas[0]
            coordenadas[3] -= coordenadas[1]
            tupla = tuple(coordenadas)
            # print(tupla)

            im1 = pyautogui.screenshot(region=tupla)

            im1 = ImageTk.PhotoImage(im1)

            # Add the image in the canvas widget
            image1 = Label(my_canvas, image=im1)
            image1.image = im1

            my_canvas.create_window(0, 0, window=image1, anchor=NW)       

            coordenadas.clear()
            ventana.deiconify()


    # Ventana Transparente
    ventana_transparente = Toplevel()
    ventana_transparente.attributes('-alpha',0.1)
    ventana_transparente.attributes('-fullscreen', True)
    ventana_transparente.bind("<Button-1>", get_event)


# Define a function to take the screenshot
def take_screenshot(ventana,my_canvas):
    ventana.iconify()
    time.sleep(0.5)
    altura_pantalla = ventana.winfo_screenheight()
    ancho_pantalla = ventana.winfo_screenwidth()
    im1 = pyautogui.screenshot(region = (0,0,ancho_pantalla,altura_pantalla))

    # Abrir nueva ventana con la imagen
    # top = Toplevel(ventana)
    im1 = ImageTk.PhotoImage(im1)

    # global my_canvas
    # my_canvas = Canvas(top, width= (coordenadas[2]), heigh= (coordenadas[3]), bg="white")
    # my_canvas.pack()

    # Add the image in the canvas widget
    image1 = Label(my_canvas, image=im1)
    image1.image = im1

    my_canvas.create_window(0, 0, window=image1, anchor=NW)     

    ventana.deiconify()
