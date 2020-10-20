from tkinter import *
from scrollClass import ScrollableFrame


'''Cuenta:
Es la lista de los items que el cliente va pidiendo
'''

class cuenta:
	def __init__(self,root,lista):
		self.frame=Frame(root)
		self.lista=lista
		self.total=0
		self.frameInternoCuenta=Frame(self.frame)
		self.frameInternoCuenta.pack(expand=True,fill="both")
		self.frameCuenta()



	def frameCuenta(self):	
		contador=0
		self.frameInternoCuenta.pack_forget()
		self.frameInternoCuenta=ScrollableFrame(self.frame)
		self.frameInternoCuenta.pack(expand=True,fill="both")
		r=1

		#Metodos internos: 
		def single_view(paquete):
			frame=self.frameInternoCuenta.scrollable_frame
			lbl=Button(frame,text=paquete[0],font=("Serif",20),
				command=lambda r=r:self.borrarLinea(r))
			lbl.grid(row=r,column=0,sticky="nsew")
			lbl_precio=Label(frame,text="$ "+str(paquete[1]),
				font=("Serif",20,"bold italic"))
			lbl_precio.grid(row=r,column=1,sticky="e")

		def definirTotal():
			self.total=contador

			lbl_total=Label(self.frameInternoCuenta.scrollable_frame,
			text="Total: "+str(contador),bg="Black",fg="white",
				font=("Serif",24,"bold italic"))
			lbl_total.grid(row=0,columnspan=3,sticky="nsew")	
			

		for paquete in self.lista:
			single_view(paquete)
			contador=contador+paquete[1]
			r=r+1

		definirTotal()


	def limpiarDatos(self):
		self.lista=[]
		self.total=0
		self.frameInternoCuenta.pack_forget()


	def borrarLinea(self,r):
		self.lista.pop(r-1)
		self.frameCuenta()	
