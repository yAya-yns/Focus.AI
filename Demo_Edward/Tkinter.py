import tkinter as tk
root = tk.Tk()
T = tk.Text(root, height=2, width=30)
T.pack()
T.insert(tk.END, "Just a text Widget\nin two lines\n")
tk.mainloop()


# win = tk.Tk()
# # win.geometry("600x250")
# T = tk.Text(win, height=2, width=30)
# T.pack()
# T.insert(tk.END, "Just a text Widget\nin two lines\n")
#
# win.eval('tk::PlaceWindow . center')
#
# win.mainloop()
