from tkinter import *



root=Tk()

firma=StringVar()

def metodo(i):
	print("Variable recibida: ",i)

for i in range(0,5):
	entry_firma=Entry(root,
		show="$")
	entry_firma.bind('<Return>',lambda event, i=i:metodo(i))
	entry_firma.pack()

root.mainloop()