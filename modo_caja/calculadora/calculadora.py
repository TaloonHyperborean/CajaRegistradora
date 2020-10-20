from tkinter import *

class calcu:
	def __init__(self,root,frame):
		self.root=root
		self.frame=Frame(frame)
		self.num=StringVar()


	def construirCalculadora(self):
		j=0
		r=1
		lbl_pantalla=Label(self.frame,textvariable=self.num,
			bg="black",fg="white",
			font=("Serif",22,"bold italic"))
		lbl_pantalla.grid(row=0,columnspan=4,sticky="nsew")
		for i in range(0,10):
			if(j>2):
				j=0

			if(i==3 or i==6 or i==9):
				#
				r=r+1

			j=j+1	
				
			num=i
			btn=Button(self.frame,text=i,font=("Serif",30,"bold italic"),
				command=lambda num=num:self.elegirBoton(num),bd=3,
				bg="#050180",fg="white")
			btn.grid(row=r,column=j,padx=2,pady=2,sticky="nsew")	
	
		btn_borrar=Button(self.frame,text="Borrar",
			command=lambda:self.borrar(),
			font=("Serif",20,"bold italic"))
		btn_borrar.grid(row=4,column=2,columnspan=2,sticky="nsew")


	def elegirBoton(self,num):
		valor_antiguo=self.num.get()
		if(valor_antiguo==0):
			self.num.set(num)
		else:
			new_valor=valor_antiguo+str(num)
			self.num.set(new_valor)

	def borrar(self):
		numeroActual=self.num.get()
		longitud=len(self.num.get())
		new=numeroActual[0:longitud-1]
		self.num.set(new)	




			
		
