from tkinter import *
from promos.qr import QrClass
import hashlib
from BD_productos.bd_promotores import bd_promotores
from tkcalendar import DateEntry
import Constantes


class nuevaPromocion:
	def __init__(self,root,ventana):
		self.root=root
		self.ventana=ventana
		self.frame=Frame(root,bg="#570532")
		self.promotor=StringVar()
		self.descripcion=Label(self.frame)
		self.cantidad=IntVar()
		self.cantidad.set(1)
		self.firma=StringVar()
		self.bd=bd_promotores()
		self.crearFrameNuevaProm()

	def crearFrameNuevaProm(self):
		#Declaracion de variables
		self.frameSuperior=Frame(self.frame,bg="#570532")
		self.frameMedio=Frame(self.frame,bg="#570532")
		frameInterno=Frame(self.frame,bg="#570532")

		#Metodos internos: 
		def FrameMedio():
			def opcionCaduca():
				self.qr_caduco=True
				lbl_valido_hasta.pack(fill="x")
				self.fechaCaducidad.pack()
				lbl_cantidad.pack_forget()
				self.entry_cantidad.pack_forget()

			def opcionEdicionLimitada():
				self.qr_caduco=False
				lbl_cantidad.pack(fill="x",expand=True)
				self.entry_cantidad.pack(fill="both")
				self.fechaCaducidad.pack_forget()
				lbl_valido_hasta.pack_forget()


			btn_caducidad=Button(self.frameMedio,text="Por caducidad",
				bg="#8D4D09",fg="white",font=("Courier",20,"bold italic"),
				command=lambda:opcionCaduca())
			btn_caducidad.pack(side="left",padx=5,pady=5,
				expand=False,fill="x")

			btn_edicionLim=Button(self.frameMedio,text="Edicion limitada",
				bg="#8B8D09",fg="white",font=("Courier",20,"bold italic"),
				command=lambda:opcionEdicionLimitada())
			btn_edicionLim.pack(side="left",padx=5,pady=5,
				expand=False,fill="x")

			lbl_valido_hasta=Label(self.frameMedio,text="Valido hasta:",
				font=("Courier",24,"bold italic"),
					bg="#570532",fg="white")
			self.fechaCaducidad=DateEntry(self.frameMedio)
			lbl_cantidad=Label(frameInterno,text="Cantidad a emitir:",
					font=("Courier",24,"bold italic"),bg="#570532",fg="white")
			
			self.entry_cantidad=Entry(frameInterno,textvariable=self.cantidad,
					font=("Courier",24,"bold italic"),fg="white")

		self.crearBotonElegirPromocion()

		lbl_tipoProm=Label(self.frameSuperior,text="Tipo de Prom:",
			font=("Courier",24,"bold italic"),
			bg="#570532",fg="white")
		lbl_tipoProm.pack(fill="x")

		FrameMedio()

		self.frameSuperior.pack(fill="x",expand=False)
		self.frameMedio.pack(fill="x",expand=False)
		frameInterno.pack(fill="both",expand=False)

		
		self.crearFrameFirmaPermiso()
		self.crearBotonAtras()
		

	def crearFrameFirmaPermiso(self):
		self.firma=StringVar()

		def calcularHashQr():
			print(self.fechaCaducidad.get_date())
			guess=f'{self.HashPromocion}{self.fechaCaducidad.get_date()}{self.firma.get()}{self.Promotor[4]}'.encode()
			
			calcu=hashlib.sha256()
			calcu.update(guess)
			
			self.crearCodigos(calcu.hexdigest())

		framePermiso=Frame(self.frame,bg="#570532")
		lbl_ingresa_firma=Label(framePermiso,text="Ingresa tu firma",
			font=("Serif",24,"bold italic"),bg="#570532",fg="white")
		lbl_ingresa_firma.pack(fill="x",expand=True)

		entry_firma=Entry(framePermiso,textvariable=self.firma,
			show="$")
		entry_firma.bind('<Return>',lambda event:calcularHashQr())
		entry_firma.pack()
		framePermiso.pack(fill="x")


	def crearBotonElegirPromocion(self):
		frameInterno=Frame(self.frameSuperior,bg="#570532")

		def packFrame():
			#self.frame.pack_forget()
			frameInterno.pack()

		def calcularHashPromocion(promocion):
			guess=f'{promocion["descuento"]}{promocion["descripcion"]}'.encode()
			calculo=hashlib.sha256()
			calculo.update(guess)
			return calculo.hexdigest()	

		def elegirPromocion(promocion):
			self.HashPromocion=calcularHashPromocion(promocion)
			self.frame.pack(fill="both",expand=True)
			frameInterno.pack_forget()
			
				
		btn=Button(self.frameSuperior,text="Elegir promocion",
			font=("Serif",22,"bold italic"),bg="#325705",fg="white",
			command=lambda:packFrame())
		btn.pack()
		
		for promocion in Constantes.promociones:
			btn=Button(frameInterno,text=promocion["descripcion"],
				font=("Serif",22,"bold italic"),bg="#530557",fg="white",
				command=lambda promocion=promocion:elegirPromocion(promocion))
			btn.pack(fill="x",padx=5,pady=5)

	def crearCodigos(self,hashQR):	
		lista=self.bd.leerTodo()	
		if(self.qr_caduco):
			#Es un cupon caduco:
			  #-Solo es necesario 1 
			newCode=QrClass(self.Promotor,hashQR)
			newCode.codigo_caducidad(self.fechaCaducidad.get_date())
		else:
			#Es un cupon edicion limitada:
			 #-Tienes que dar un loop para crear uno por uno
			for i in range(0,self.cantidad.get()):				
				newCode=QrClass(self.Promotor,hashQR)
				newCode.crearCodigo(2)
				res=self.promocionRepetida(lista,resultado)
				if (res==False):
					print("Hash resultado producido: ",resultado)
					self.bd.crear(self.promotor.get(),resultado,str(i))



	def promocionRepetida(self,lista,resultadoHash):
		respuesta=False
		for promocion in lista:
			
			if(promocion[2]==resultadoHash):
				print("Promocion repetida: ",resultadoHash[:7])
				respuesta=True
				break

		return respuesta		

	def crearBotonAtras(self):
		boton=Button(self.frame,text="Atras",font=("Courier",20),
			bg="red",fg="white",
			command=lambda:self.atras())
		boton.pack(side="left",anchor="s")	

	def atras(self):
		#Neutralizo los campos
		self.cantidad.set("")
		self.frame.pack_forget()
		self.ventana.frame.pack(fill="both",expand=True)

