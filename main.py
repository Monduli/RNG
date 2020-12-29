import tkinter as tk
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
		tk.Label(self._master, text="Number 1").grid(row=0)
		tk.Label(self._master, text="Number 2").grid(row=1)
		self.to_set = tk.Label(self._master, text=self.result_text)
		self.text1 = tk.Entry(self._master)
		self.text1.grid(row=0, column=1)
		self.text2 = tk.Entry(self._master)
		self.text2.grid(row=1, column=1)
		self.button = tk.Button(text='Pick a number!', command=self.result).grid(row=2, column=0)

	def result(self):
		"""
		Calculates the result given the two input numbers.
		"""
		x = int(self.text1.get())
		y = int(self.text2.get())
		print(x, y)
		result = random.randint(x, y)
		self.result_text = "Result: " + str(result) + "."
		self.to_set = tk.Label(self._master, text=self.result_text, padx=6)
		self.to_set.grid(row=2, column=1)

#create window
#with two input spaces
#with text "Please enter 2 numbers. A number in this range will be produced."
window = tk.Tk()
canvas = tk.Canvas(window, width=400, height=300)
app = Application(window)
app.mainloop()

#display result