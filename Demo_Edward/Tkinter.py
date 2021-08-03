# import tkinter as tk
#
# root = tk.Tk()
# T = tk.Text(root, height=2, width=30)
# T.pack()
# T.insert(tk.END, "Just a text Widget\nin two lines\n")
# tk.mainloop()

#Import the tkinter library
from tkinter import *

#Create an instance of tkinter frame
win = Tk()

#Set the geometry
win.geometry("600x250")

win.eval('tk::PlaceWindow . center')

win.mainloop()
