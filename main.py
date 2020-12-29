import tkinter as tk
import random


#create window
#with two input spaces
#with text "Please enter 2 numbers. A number in this range will be produced."
window = tk.Tk()
#get numbers
x = 2 #input1
y = 4 #input2
#generate result
result = random.randint(x, y)
#display result