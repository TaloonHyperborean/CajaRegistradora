from tkinter import *
from scrollClass import ScrollableFrame
from modo_caja.pago.pantallaPago import pantallaPago
from modo_caja.cuenta.cuenta import cuenta
import Constantes

class modoCaja:
	def __init__(self,root,ventana):
		self.root=root
		self.ventana=ventana
		self.frame=Frame(root)
		self.lista=[]

		self.hamburgesas=Constantes.hamburgesas
		self.tacos=Constantes.tacos
		self.complementos=Constantes.complementos
		self.hotdogs=Constantes.hotdogs

		self.frameOpciones=Frame(self.frame,bg="blue")
		self.frameSecundario=Frame(self.frameOpciones)

		self.cuenta=cuenta(self.frame,self.lista)
		self.modoPago=pantallaPago(self)

		self.crearModoCaja()
		
		



	def crearModoCaja(self):
		frameMenu=Frame(self.frame,bg="green")
		frameMenu.pack(side="top",expand=False,fill="x",anchor="n")
		self.crearMenu(frameMenu)

		self.cuenta.frame.pack(side="left",expand=True,fill="both")
		
		self.frameOpciones.pack(side="left",expand=True,fill="y")

		self.botonAdicional=Button(self.frame,text="Adicional",
			bg="purple",fg="white",font=("Serif",24))
		self.botonAdicional.pack(expand=True,
			side="bottom",fill="x",anchor="n",padx=3,pady=15)

		self.botonPagar=Button(self.frame,text="Pagar",
			bg="orange",fg="white",font=("Serif",24,"bold italic"),
			command=lambda:self.cambiarModoPago())
		self.botonPagar.pack(expand=True,
			side="bottom",fill="x",anchor="n",padx=3,pady=15)

		self.boton_atras=Button(self.frame,text="Atras",
			bg="red",fg="white",font=("Serif",24,"bold italic"),
			command=lambda:self.atras())
		self.boton_atras.pack(expand=True,
			side="bottom",fill="x",anchor="n",padx=3,pady=15)

	

	def cambiarModoPago(self):
		self.modoPago=pantallaPago(self)
		self.modoPago.frame.pack(expand=True,fill="both")
		self.frame.pack_forget()		

	def crearMenu(self,frame):
		menu=Constantes.menu

		def elegirOpcionMenu(cont):

			#Metodo interno para llenar con los botones correspondientes
			#a la opcion de menu seleccionada.
			def llenar(lista_menu):
				self.frameSecundario.pack(fill="both",expand=True)
				c=0
				r=0
				for i in range(0,len(lista_menu)):
					if(c==2):
						c=0
						r=r+1
					paquete=lista_menu[i]	
					btn=Button(self.frameSecundario,text=lista_menu[i][0],
					font=("Serif",25,"bold italic"),
					command=lambda paquete=paquete:self.agregar(paquete))
					btn.grid(row=r,column=c,sticky="nsew",padx=1,pady=1)	
					c=c+1	

			self.frameSecundario.pack_forget()
			if(cont==1):
				llenar(self.tacos)
			elif(cont==2):	
				llenar(self.complementos)
			elif(cont==3):	
				llenar(self.hamburgesas)
			elif(cont==4):	
				llenar(self.hotdogs)	



		cont=1	
		for x in menu:
			btn=Button(frame,text=x,
				command=lambda cont=cont:elegirOpcionMenu(cont),
				bg="#0E0E73",fg="white",font=("Serif",23,"bold italic"))
			btn.pack(side="left",fill="both",expand=True)
			cont=cont+1

	def agregar(self,paquete):
		self.cuenta.lista.append(paquete)
		self.cuenta.frameCuenta()
			
	def crearBtnAtras(self):
		btn_atras=Button(self.frame,text="Atras",bg="red",fg="white",
			command=lambda:self.atras())
		btn_atras.pack(side="right",anchor="n",padx=5,pady=5)		

	def atras(self):
		self.frame.pack_forget()
		self.ventana.frame.pack(expand=True,fill="both")