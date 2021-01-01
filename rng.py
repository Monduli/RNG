#This program was written by @Monduli
#Stealing it doesn't benefit anyone as it was not difficult to make
#Just make it yourself if you're going to bother stealing it
#At least then you can learn a tiny bit about tkinter

import tkinter as tk
from tkinter.ttk import *
import random

class Application(tk.Frame):
	def __init__(self, master=None):
		super().__init__(master)
		self._master = master
		self.result_text = ""
		self.create_widgets()
		

	def create_widgets(self):
		"""
		Creates the buttons and input areas.
		"""
		# the display has 2 entry fields with 2 labels
		# and a button that generates the random number
		tk.Label(self._master, text="Number 1").grid(row=0)
		tk.Label(self._master, text="Number 2").grid(row=1)
		self.to_set = tk.Label(self._master, text=self.result_text)
		self.to_set.grid(row=2, column=1)
		self.text1 = tk.Entry(self._master)
		self.text1.grid(row=0, column=1)
		self.text2 = tk.Entry(self._master)
		self.text2.grid(row=1, column=1)
		self.button = tk.Button(text='Pick a number!', command=self.result).grid(row=2, column=0)


	def result(self):
		"""
		Calculates the result given the two input numbers.
		"""
		# gets the inputs
		x = int(self.text1.get())
		y = int(self.text2.get())
		# generates the random number
		result = random.randint(x, y)
		# formats the string
		self.result_text = "Result: " + str(result) + "."
		# puts the text on the screen
		self.to_set['text'] = self.result_text

# create the window
window = tk.Tk()
window.title("RNG")
window.iconbitmap("free-d8.ico")

#experimental - need to fix
canvas = tk.Canvas(window, width=400, height=300)

#creates the application in the window
app = Application(window)
#run it
app.mainloop()
