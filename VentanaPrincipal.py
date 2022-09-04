from tkinter import *
from tkinter import filedialog
from unicodedata import name
from Fuente_Texto import Fuentes 
from calculator import open_calculator
from PIL import ImageTk, Image
from Funcion_buscador import open_browser
from Lapiz import Paint


ventana=Tk()    
ventana.title("Pizarra Virtual")
ventana.geometry('500x250')

#-------------IMAGENES--------------------
imagen_engranaje = PhotoImage(file = r'./iconos/icono-engranaje.png')
imagen_lapiz = PhotoImage(file = r'./iconos/icono-lapiz.png')

icono_file_drive = PhotoImage(file = r'./iconos/icono-drive.png')
icono_file_visualizar = PhotoImage(file = r'./iconos/icono-visualizar.png')
icono_file_upload = PhotoImage(file = r'./iconos/icono-upload-file.png')
icono_file_download = PhotoImage(file = r'./iconos/icono-download-file.png')

icono_edit_color = PhotoImage(file = r'./iconos/icono-color_lapiz-edit.png')
icono_edit_borrar = PhotoImage(file = r'./iconos/icono-borrar-edit.png')
icono_edit_guardar = PhotoImage(file = r'./iconos/icono-guardar-edit.png')
icono_edit_italica = PhotoImage(file = r'./iconos/icono-italica-edit.png')
icono_edit_negrita = PhotoImage(file = r'./iconos/icono-negrita-edit.png')
icono_edit_subrayar = PhotoImage(file = r'./iconos/icono-subrayar-edit.png')

icono_tools_calculadora = PhotoImage(file = r'./iconos/icono-calculadora-tools.png')
icono_tools_internet = PhotoImage(file = r'./iconos/icono-internet-tools.png')
icono_tools_recortar = PhotoImage(file = r'./iconos/icono-recortar-tools.png')
icono_tools_reglas = PhotoImage(file = r'./iconos/icono-reglas-tools.png')

icono_window_newwindow = PhotoImage(file = r'./iconos/icono-window.png')

#--------------CONTADORES----------------
contador_opciones = 0
contador_lapiz = 0

contador_file = 0
contador_edit = 0
contador_options = 0
contador_herramientas = 0
contador_window = 0
contador_new_window = 0

contador_edit_estilos_texto = 0
contador_edit_italica = 0
#----------FUNCIONES DE BOTONES------------
global funcion_opciones
def funcion_opciones():
    global contador_opciones
    contador_opciones = contador_opciones + 1

    if contador_opciones == 1 :
        global etiqueta_menu_opciones
        etiqueta_menu_opciones=Label(ventana, bg = "light gray")
        boton_archivo = Button(etiqueta_menu_opciones, text = "  File  ", border = 1, command = funcion_file )
        boton_archivo.pack(side = LEFT)

        boton_editar = Button(etiqueta_menu_opciones, text = "  Edit  ", border = 1, command = funcion_edit )
        boton_editar.pack(side = LEFT)

        boton_options = Button(etiqueta_menu_opciones, text = "  Options  ", border = 1, command = funcion_options )
        boton_options.pack(side = LEFT)

        boton_herramientas = Button(etiqueta_menu_opciones, text = "  Tools  ", border = 1, command = funcion_herramientas )
        boton_herramientas.pack(side = LEFT)

        boton_ventana = Button(etiqueta_menu_opciones, text = "  Window  ", border = 1, command = funcion_windows )
        boton_ventana.pack(side = LEFT)
        
        etiqueta_menu_opciones.pack(fill = X)
    if contador_opciones == 2 :
        contador_opciones = 0
        etiqueta_menu_opciones.pack_forget()

#----------FUNCIONES DE LAPIZ--------------
def funcion_lapiz():
    global contador_lapiz
    contador_lapiz = contador_lapiz + 1
    Paint()
#   DAR USO AL CONTADOR - SINO, BORRAR    

#--------------FUNCIONES DE OPCIONES -----------
def funcion_file ():
    global contador_file
    contador_file= contador_file + 1
    if contador_file == 1:
        global etiqueta_menu_file
        etiqueta_menu_file=Label(ventana)
        
        boton_drive = Button(etiqueta_menu_file, image = icono_file_drive, borderwidth = 0)
        boton_drive.pack(side = LEFT)

        boton_ver = Button(etiqueta_menu_file, image = icono_file_visualizar, borderwidth = 0)
        boton_ver.pack(side = LEFT)

        boton_subir = Button(etiqueta_menu_file, image = icono_file_upload, borderwidth = 0, command = funcion_file_abrir)
        boton_subir.pack(side = LEFT)

        boton_descargar = Button(etiqueta_menu_file, image = icono_file_download, borderwidth = 0)
        boton_descargar.pack(side = LEFT)
        
        etiqueta_menu_file.pack(fill = X)
        
        if contador_edit == 1 :
            etiqueta_menu_edit.pack_forget()
        if contador_options == 1 :
            etiqueta_menu_options.pack_forget()
        if contador_herramientas == 1 :
            etiqueta_menu_tools.pack_forget()
        if contador_window == 1 :
            etiqueta_menu_window.pack_forget()

    if contador_file == 2 :
        contador_file = 0
        etiqueta_menu_file.pack_forget()


def funcion_edit ():
    global contador_edit
    contador_edit = contador_edit + 1
    if contador_edit == 1:
        global etiqueta_menu_edit
        etiqueta_menu_edit = Label(ventana)
        
        boton_lapiz = Button(etiqueta_menu_edit, image = icono_edit_color, borderwidth = 0)
        boton_lapiz.pack(side = LEFT)

        boton_texto = Button(etiqueta_menu_edit, text = "  Text style  ", command = funcion_edit_estilo_texto, border = 1 )
        boton_texto.pack(side = LEFT)

        boton_guardar = Button(etiqueta_menu_edit, image = icono_edit_guardar, borderwidth = 0)
        boton_guardar.pack(side = LEFT)
        
        boton_borrar = Button(etiqueta_menu_edit, image = icono_edit_borrar, borderwidth = 0)
        boton_borrar.pack(side = LEFT)

        etiqueta_menu_edit.pack(fill = X)

        if contador_file == 1 : 
            etiqueta_menu_file.pack_forget()
        if contador_options == 1 :
            etiqueta_menu_options.pack_forget()
        if contador_herramientas == 1 :
            etiqueta_menu_tools.pack_forget()
        if contador_window == 1 :
            etiqueta_menu_window.pack_forget()

    if contador_edit == 2 :
        contador_edit = 0
        etiqueta_menu_edit.pack_forget()

def funcion_options ():
    global contador_options
    contador_options = contador_options + 1
    if contador_options == 1:
        global etiqueta_menu_options
        etiqueta_menu_options=Label(ventana)
        
        boton_pizarra_izq = Button(etiqueta_menu_options, text = "  Left Board  ", border = 1 )
        boton_pizarra_izq.pack(side = LEFT)

        boton_pizarra_der = Button(etiqueta_menu_options, text = "  Right Board  ", border = 1 )
        boton_pizarra_der.pack(side = LEFT)
        
        etiqueta_menu_options.pack(fill = X)

        if contador_file == 1 : 
            etiqueta_menu_file.pack_forget()
        if contador_edit == 1 :
            etiqueta_menu_edit.pack_forget()
        if contador_herramientas == 1 :
            etiqueta_menu_tools.pack_forget()
        if contador_window == 1 :
            etiqueta_menu_window.pack_forget()

    if contador_options == 2 :
        contador_options = 0
        etiqueta_menu_options.pack_forget()

def funcion_herramientas ():
    global contador_herramientas
    contador_herramientas = contador_herramientas + 1
    if contador_herramientas == 1:
        global etiqueta_menu_tools
        etiqueta_menu_tools=Label(ventana)
        
        boton_calculadora = Button(etiqueta_menu_tools, image = icono_tools_calculadora,command = open_calculator, borderwidth = 0)
        boton_calculadora.pack(side = LEFT) 

        boton_internet = Button(etiqueta_menu_tools, image = icono_tools_internet, command = open_browser ,borderwidth = 0)
        boton_internet.pack(side = LEFT)

        boton_recortar = Button(etiqueta_menu_tools, image = icono_tools_recortar, borderwidth = 0)
        boton_recortar.pack(side = LEFT)
        
        boton_regla = Button(etiqueta_menu_tools, image = icono_tools_reglas, borderwidth = 0)
        boton_regla.pack(side = LEFT)

        etiqueta_menu_tools.pack(fill = X)

        if contador_file == 1 : 
            etiqueta_menu_file.pack_forget()
        if contador_edit == 1 :
            etiqueta_menu_edit.pack_forget()
        if contador_options == 1 :
            etiqueta_menu_options.pack_forget()
        if contador_window == 1 :
            etiqueta_menu_window.pack_forget()

    if contador_herramientas == 2:
        contador_herramientas = 0
        etiqueta_menu_tools.pack_forget()

def funcion_windows ():
    global contador_window
    contador_window = contador_window + 1
    if contador_window == 1:
        global etiqueta_menu_window
        etiqueta_menu_window=Label(ventana)
        
        boton_new_board = Button(etiqueta_menu_window, image = icono_window_newwindow, borderwidth = 0, command = funcion_window)
        boton_new_board.pack(side = LEFT)

        etiqueta_menu_window.pack(fill = X)
        
        if contador_file == 1 : 
            etiqueta_menu_file.pack_forget()
        if contador_edit == 1 :
            etiqueta_menu_edit.pack_forget()
        if contador_options == 1 :
            etiqueta_menu_options.pack_forget()
        if contador_herramientas == 1 :
            etiqueta_menu_tools.pack_forget()

    if contador_window == 2:
        contador_window = 0
        etiqueta_menu_window.pack_forget()

#-------------FUNCIONES DE FILE ------------------
def funcion_file_abrir() :
    ventana.filename = filedialog.askopenfilename(initialdir = './iconos', title = 'Select a jpg or png document', filetypes = (("png files", "*.png"),("jpg files", "*.jpeg")))
    Etiqueta_imagen = Label(ventana, text = ventana.filename)
    Etiqueta_imagen.pack()
    Imagen1 = ImageTk.PhotoImage(Image.open(ventana.filename))
    Imagen_etiqueta = Label(image = Imagen1)
    Imagen_etiqueta.pack()

#-------------FUNCIONES DE WINDOW-----------------
def funcion_window () :
    global contador_new_window
    contador_new_window = contador_new_window + 1
    name = 'ventana' + str(contador_new_window)
    name = Tk()    
    name.title("Pizarra Virtual " + str(contador_new_window))
    
    name_label = "etiqueta_opciones" + str(contador_new_window)
    name_label=Label(name)
    name_label.pack(fill=X)
    


    

#--------------FUNCIONES DE EDIT-------------
def funcion_edit_estilo_texto ():
    global contador_edit_estilos_texto
    contador_edit_estilos_texto = contador_edit_estilos_texto + 1
    if contador_edit_estilos_texto == 1:
        global etiqueta_menu_edit_estilo_texto
        etiqueta_menu_edit_estilo_texto=Label(ventana)
        boton_edit_italica = Button(etiqueta_menu_edit_estilo_texto, image = icono_edit_italica, borderwidth = 0)
        boton_edit_italica.pack(side = LEFT)

        boton_edit_negrita = Button(etiqueta_menu_edit_estilo_texto, image = icono_edit_negrita, borderwidth = 0)
        boton_edit_negrita.pack(side = LEFT)

        cajadesplegable_fuente_texto = StringVar()
        cajadesplegable_fuente_texto.set("  Source  ")
        desplegable = OptionMenu(etiqueta_menu_edit_estilo_texto, cajadesplegable_fuente_texto, *Fuentes)
       
        desplegable.pack()

        etiqueta_menu_edit_estilo_texto.pack(fill = X)
        Texto = Entry(ventana, width = 50)
        Texto.pack()

        if contador_file == 1 : 
            etiqueta_menu_file.pack_forget()
        if contador_options == 1 :
            etiqueta_menu_options.pack_forget()
        if contador_herramientas == 1 :
            etiqueta_menu_tools.pack_forget()
        if contador_window == 1 :
            etiqueta_menu_window.pack_forget()

    if contador_edit_estilos_texto == 2 :
        contador_edit_estilos_texto = 0
        etiqueta_menu_edit.pack_forget()

def funcion_edit_italica() :
    global contador_edit_italica
    contador_edit_italica = contador_edit_italica + 1

#-----------------BOTONES---------------
etiqueta_opciones=Label(ventana)
etiqueta_opciones.pack(fill=X)

boton_engranaje=Button(etiqueta_opciones, image = imagen_engranaje, command = funcion_opciones, borderwidth = 0)
boton_engranaje.pack(side = LEFT)

boton_lapiz=Button(etiqueta_opciones, image = imagen_lapiz, command = funcion_lapiz, borderwidth = 0)
boton_lapiz.pack(side = RIGHT)


ventana.mainloop()