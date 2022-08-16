from tkinter import *
from tkinter.ttk import *

def open_browser():
	import webbrowser
	import re
	
	global Buscador
	Buscador = Toplevel()
	Buscador.title("Buscador")
	Buscador.geometry("350x40")
	Buscador.resizable(0,0)

	global Var
	Var = StringVar()

	global pattern
	pattern = r"^(https?:\/\/)?([\da-z\.-]+)\.([a-z\.]{2,6})([\/\w \.-]*)*\/?$"
	
		
	def fun_enter(event):
		match = re.search(pattern, Var.get())

		if match:
			webbrowser.open_new(match.group())
		else:
			webbrowser.open_new_tab("https://www.google.com/search?q=" + Var.get())
		return
	

	global image_enter
	image_enter = PhotoImage(file = r'./iconos/enter.png')
	image_enter = image_enter.subsample(25,25)

	
	global enter_btn
	enter_btn = Button(Buscador, image=image_enter, command = lambda: fun_enter(1))
	enter_btn.grid(row=0, column=2, sticky=E)


	global search_input
	search_input = Entry(Buscador, textvariable= Var, width=50)
	search_input.focus()
	search_input.grid(row=0, column=1)

	search_input.bind('<Return>', fun_enter)
	
