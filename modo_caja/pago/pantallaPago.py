from tkinter import *
from scrollClass import ScrollableFrame
from modo_caja.calculadora.calculadora import calcu
from modo_caja.cuenta.cuenta import cuenta
import json
import os
import time
from datetime import date
from promos.validar_promocion import ValidarPromocion

class pantallaPago:
	def __init__(self,cajaRegistradora):
		self.root=cajaRegistradora.root
		self.frame=Frame(self.root)
		self.total=cajaRegistradora.cuenta.total
		self.lista=cajaRegistradora.cuenta.lista
		self.cuenta=cuenta(self.frame,self.lista)
		self.cajaRegistradora=cajaRegistradora
		
		
		self.calcu=calcu(self.root,self.frame)
		self.lbl_cambio=Label(self.frame,font=("Serif",30,"bold italic"),
				bg="#730E19",fg="white")

		self.validarPromocion=ValidarPromocion(self.root,self)
		
		self.framePantallaPago()


	def framePantallaPago(self):
		self.cuenta.frame.pack(side="left",expand=True,fill="both")
		self.calcu.construirCalculadora()
		self.calcu.frame.pack(expand=True,side="left",
			fill="both",padx=10,pady=10)

		self.frameBotones=Frame(self.frame)
		self.frameBotones.pack(expand=True,fill="y",side="right")

		btn_atras=Button(self.frameBotones,text="Atras",font=("Serif",20,"bold italic"),
			bg="red",fg="white",command=lambda:self.atras())
		btn_atras.pack(fill="both",padx=10,pady=5)


		btn_exacto=Button(self.frameBotones,text="Exacto",font=("Serif",22),
			bg="#2A0254",fg="white",command=lambda:self.exacto())
		btn_exacto.pack(fill="both",padx=10,pady=5)

		def botones_cantidades():
			btn_100=Button(self.frameBotones,text="$100",font=("Serif",22),
				bg="#095B02",fg="white",command=lambda:self.otraCantidad(100))
			btn_100.pack(fill="both",expand=True,padx=5,pady=5)

			btn_200=Button(self.frameBotones,text="$200",font=("Serif",22),
				bg="#095B02",fg="white",command=lambda:self.otraCantidad(200))
			btn_200.pack(fill="both",expand=True,padx=5,pady=5)
			
			btn_500=Button(self.frameBotones,text="$500",font=("Serif",22),
				bg="#095B02",fg="white",command=lambda:self.otraCantidad(500))
			btn_500.pack(fill="both",expand=True,padx=5,pady=5)

		botones_cantidades()
		btn_tarjeta=Button(self.frameBotones,text="Tarjeta",font=("Serif",22),
			bg="#5B0256",fg="white")
		btn_tarjeta.pack(fill="both",padx=5,pady=5)

		def cambiarPantalla():
			self.frame.pack_forget()
			self.validarPromocion.frame.pack(fill="both",expand=True)

		btn_validar_prom=Button(self.frameBotones,text="Validar\nCupon",
			font=("Serif",22),bg="#5B0256",fg="white",
			command=lambda:cambiarPantalla())
		btn_validar_prom.pack(fill="both",padx=5,pady=5)

	def exacto(self):
		total=self.cuenta.total
		numeroCalculadora=self.calcu.num.get()
		if(numeroCalculadora==''):
			resultado=0

		else:
			valor=int(numeroCalculadora)
			resultado=valor-total
				

		if(resultado<0):
			return
		else:
			self.crearTicket(total)
			if(resultado!=0):
				#Si existe un cambio que dar.
				texto="Cambio: "+str(resultado)
				self.lbl_cambio.config(text=texto)
				self.lbl_cambio.pack()
				self.botonReinicio()
			else:
				self.reinicio()	

	def otraCantidad(self,cantidad):
		total=self.cuenta.total

		cambio=cantidad-total
		
		if(cambio>0):
			self.crearTicket(total)
			texto="Cambio: "+str(cambio)
			self.lbl_cambio.config(text=texto)
			self.lbl_cambio.pack()
			self.botonReinicio()

		else:
			#El cambio no debe ser negativo, al cliente
			#le hace falta pagar
			texto="Falta por\npagar: "+str(cambio)
			self.lbl_cambio.config(text=texto)
			self.lbl_cambio.pack()




	def botonReinicio(self):
		btn_reinicio=Button(self.frame,text="Salir",bg="red",fg="white",
			font=("Courier",22,"bold italic"),
			command=lambda:self.reinicio())
		btn_reinicio.pack(padx=3,pady=3)

	def atras(self):
		self.frameBotones.pack_forget()
		self.frame.pack_forget()

		self.cajaRegistradora.frame.pack(fill="both",expand=True)


	def reinicio(self):
		#Vaciar lista
		self.lista=[]
		self.cajaRegistradora.cuenta.frameInternoCuenta.pack_forget()
		self.cajaRegistradora.cuenta.lista=[]
		self.frameBotones.pack_forget()
		self.frame.pack_forget()
		self.cajaRegistradora.frame.pack_forget()
		self.cajaRegistradora.ventana.frame.pack(fill="both",expand=True)
		self.cuenta.limpiarDatos()
	

	def crearTicket(self,total):
		print("Creando ticket...")
		fecha=str(date.today())
		data={
			"total":total,
			"lista":self.lista
		}
		camino_archivo='tickets/registros/'+fecha+'/'
		
		
		try:
			#
		    os.makedirs(camino_archivo)
		except OSError as e:
		    print("Ya existe ruta de esta fecha")

		index_ticket = str(len(os.listdir(camino_archivo))+1)
		with open(camino_archivo+'/'+index_ticket+'.txt', 'w') as outfile:
				
			json.dump(data, outfile)

		


		
		
		
