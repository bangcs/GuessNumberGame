import tkinter as tk
from tkinter import StringVar, ttk
import random as r

LARGEFONT =("Sans", 35)
v_tebakan = 0

class tkinterApp(tk.Tk):
	
	# __init__ function for class tkinterApp
	def __init__(self, *args, **kwargs):
		
		# __init__ function for class Tk
		tk.Tk.__init__(self, *args, **kwargs)
		
		# creating a container
		container = tk.Frame(self)
		container.pack(side = "top", fill = "both", expand = True)

		container.grid_rowconfigure(0, weight = 1)
		container.grid_columnconfigure(0, weight = 1)

		# initializing frames to an empty array
		self.frames = {}

		# iterating through a tuple consisting
		# of the different page layouts
		for F in (StartPage, Page1, Page2):

			frame = F(container, self)

			# initializing frame of that object from
			# startpage, page1, page2 respectively with
			# for loop
			self.frames[F] = frame

			frame.grid(row = 0, column = 0, sticky ="nsew")

		self.show_frame(StartPage)

	# to display the current frame passed as
	# parameter
	def show_frame(self, cont):
		frame = self.frames[cont]
		frame.tkraise()

# first window frame startpage

class StartPage(tk.Frame):

	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)
		
		# label of frame Layout 2
		label = ttk.Label(self, text ="Game Tebak Angka", font = LARGEFONT)
		entry = ttk.Entry(self)
		# putting the grid in its place by using
		# grid
		label.grid(row = 0, column = 2, padx = 10, pady = 10)

		button1 = ttk.Button(self, text ="Mulai Game",
		command = lambda : controller.show_frame(Page1))
	
		# putting the button in its place by
		# using grid
		button1.grid(row = 1, column = 2, padx = 10, pady = 10)

		## button to show frame 2 with text layout2
		button2 = ttk.Button(self, text ="Setting",
		command = lambda : controller.show_frame(Page2))
	
		# putting the button in its place by
		# using grid
		button2.grid(row = 2, column = 2, padx = 10, pady = 10)

		


# second window frame page1
class Page1(tk.Frame):
	def __init__(self,parent,controller):
		tk.Frame.__init__(self, parent)

		angkarandom = r.randint(0,10000)
		def checkinput(a):
			try :
				number = int(a)
				return number
			except :
 				return 'Error'
		
		var_a = StringVar()

		def entry_event(event):
			var_a = ngentry.get()
			utama(var_a)
			

		def utama(event)	:
			
			v_tebakan = checkinput(event)
			if type(v_tebakan) == int:
				if v_tebakan > angkarandom:
					label2.config(text = "Terlalu Besar")
				elif v_tebakan <angkarandom:
					label2.config(text = "Terlalu Kecil")
				else :
					label2.config(text = "Benarr")
			else:
				label2.config(text='Masukkan angka')


		label = ttk.Label(self, text = "Silankan Tebak Angka", font = LARGEFONT)
		ngentry = ttk.Entry(self)
		label2 = ttk.Label(self, text = "", font = LARGEFONT)
		
		button1 = ttk.Button(self, text = "Tebak",
                            command = lambda : utama(ngentry.get()))
		button2 = ttk.Button(self, text = "Kembali",
                            command = lambda : controller.show_frame(StartPage))

		ngentry.bind('<Return>', entry_event)

		label.grid  (row = 0, column = 2, padx = 10, pady = 10)
		label2.grid (row = 2, column = 2, padx = 10, pady = 10)
		ngentry.grid(row = 1, column = 2, padx = 10, pady = 10)
		button1.grid(row = 1, column = 4, padx = 10, pady = 10)
		button2.grid(row = 1, column = 0, padx = 10, pady = 10)
			
 

# third window frame page2
class Page2(tk.Frame):
	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)
		label = ttk.Label(self, text ="Page 2", font = LARGEFONT)
		label.grid(row = 0, column = 4, padx = 10, pady = 10)

		# button to show frame 2 with text
		# layout2
		button1 = ttk.Button(self, text ="Page 1",
							command = lambda : controller.show_frame(Page1))
	
		# putting the button in its place by
		# using grid
		button1.grid(row = 1, column = 1, padx = 10, pady = 10)

		# button to show frame 3 with text
		# layout3
		button2 = ttk.Button(self, text ="Startpage",
							command = lambda : controller.show_frame(StartPage))
	
		# putting the button in its place by
		# using grid
		button2.grid(row = 2, column = 1, padx = 10, pady = 10)


# Driver Code
app = tkinterApp()
app.mainloop()
