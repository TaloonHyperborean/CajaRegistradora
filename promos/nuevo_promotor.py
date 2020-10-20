from tkinter import *
from BD_productos.bd_promotores import bd_promotores
from datetime import date
import hashlib

'''Esta clase guarda y registra en la BD los datos esenciales de los
individuos que fungiran como promotores del negocio en cuestion.'''

class nuevoPromotor:
	def __init__(self,ventana,root):
		self.ventana=ventana
		self.frame=Frame(root)
		self.frame.config(bg="#13012D")
		self.prom=StringVar()
		self.address=StringVar()
		self.crearFrameNuevoPromotor()
		self.bd_promotores=bd_promotores()
		self.fecha=str(date.today())


	def crearFrameNuevoPromotor(self):
		#
		self.crearBotonAtras()
		lbl=Label(self.frame,text="Nombre del promotor",
			font=("Serif",30,"bold italic"),
			bg="#13012D",fg="white").pack(fill="x",padx=10,pady=10)

		entry=Entry(self.frame,textvariable=self.prom,
			font=("Serif",35),justify="center")		
		entry.pack(padx=20,pady=20,fill="x")

		lbl_2=Label(self.frame,text="Direccion(Ethereum)",
			font=("Serif",30,"bold italic"),
			bg="#13012D",fg="white").pack(fill="x",padx=10,pady=10)

		entry_2=Entry(self.frame,textvariable=self.address,
			font=("Serif",35),justify="center")		
		entry_2.pack(padx=20,pady=20,fill="x")


		btn=Button(self.frame,text="Crear promotor",
			bg="#C11AAF",fg="white",font=("Serif",30,"bold italic"),
			command=lambda:self.crearPromotor()).pack(padx=50,pady=50,fill="both",anchor="s")


	def crearPromotor(self):

		def calcularHash(name,address):
			guess=f'{name}{address}{self.fecha}'.encode()

			calculador=hashlib.sha256()
			calculador.update(guess)
			return calculador.hexdigest()

		def camposVacios():
			if(self.prom.get()=='' or self.address.get()==''):
				print("campos vacios")
				return False
			else:
				return True	

		nombrePromotor=self.prom.get()
		address=self.address.get()
		hashPromotor=calcularHash(nombrePromotor,address)

		#Primero verifico que los campos si tengan algo escrito.
		if(camposVacios()):
			pasa=self.filtroYaExiste(hashPromotor)
		else:
			return	

		if(pasa):
			self.bd_promotores.crear(nombrePromotor,address,
				self.fecha,hashPromotor)
			self.atras()
		else:
			lbl=Label(self.frame,text="Ya existe promotor",
			font=("Serif",30,"bold italic"),
			bg="red",fg="white").pack(fill="x",padx=10,pady=10)	
	

	def filtroYaExiste(self,hashPromotor):
		respuesta=True
		listaPromotores=self.bd_promotores.leerTodo()
		for promotor in listaPromotores:
			if(hashPromotor==promotor[4]):
				respuesta=False
				break
		return respuesta
					

	def crearBotonAtras(self):
		boton=Button(self.frame,text="Atras",font=("Courier",20,"bold italic"),
			bg="red",fg="white",
			command=lambda:self.atras())
		boton.pack(side="left",anchor="s",padx=5,pady=5)	

	def atras(self):
		self.address.set("")
		self.prom.set("")
		self.frame.pack_forget()
		self.ventana.frame.pack(fill="both",expand=True)