import os
from datetime import datetime,timedelta,date
from tkinter import filedialog,Tk
import json
from tkinter import *
from scrollClass import ScrollableFrame

class Ticket:
	def __init__(self,root,ventana):
		self.ventana=ventana
		self.frame=Frame(root)
		self.ticket=Frame(root)#Solo lo inicializo, despues lo packeo
		self.fecha=date.today()
		self.camino_archivo_fechas='registros/'
		self.configurarRutaOrginal()
		#self.directorio=os.listdir(self.camino_archivo)
		self.boton_atras=Button(self.frame,text="Atras",bg="red",fg="white",
			command=lambda:self.atras())
		self.boton_atras.pack(side="left",anchor="n")
		self.lbl_total=Label(self.frame,text="Total: 0",
			font=("Serif",20))	
		self.lbl_total.pack()
		self.num_tickets=Label(self.frame,text="Numero de tickets: 0",
			font=("Serif",20))
		self.num_tickets.pack()
		self.tiempoTicket()
		self.leerArchivo()



	def configurarRutaOrginal(self):
		try:
			self.ruta_original=os.getcwd()+'/tickets/registros/'+str(self.fecha)+'/'
			self.archivo=os.listdir(self.ruta_original)
		except Exception as e:
			print("No existe la carpeta")
			self.archivo=[]
	

	def mainFrameTicket(self):
		self.frameTicket=Frame(self.frame,bg="black")
		self.frameTicket.pack(expand=True,fill="both")

		self.frameScrollTickets=ScrollableFrame(self.frameTicket)
		self.frameScrollTickets.cambiarAncho(150)
		self.frameScrollTickets.pack(side="left",expand=False,fill="y")
		self.llenarScroll()

		self.frameSingleTicket=Frame(self.frameTicket,bg="black")
		self.frameSingleTicket.pack(side="right",expand=True,fill="both")


	def llenarScroll(self):

		def reiniciarScroll():
			self.frameScrollTickets.pack_forget()
			self.frameScrollTickets=ScrollableFrame(self.frameTicket)
			self.frameScrollTickets.pack(fill="both",side="left",expand=True)

		reiniciarScroll()
		frameScroll=self.frameScrollTickets.scrollable_frame

		if(len(self.archivo)>0):
			for filename in self.archivo:
				frameView=Frame(frameScroll,relief=SUNKEN,bd=3)
				frameView.config(bg="#180247")
				frameView.pack(padx=2,pady=2,fill="both",expand=True)
				def single_view():

					def verTicket(filename):
						#Reinicio el frame por si habia uno anterior y 
						#borrarlo
						self.frameSingleTicket.pack_forget()
						self.frameSingleTicket=Frame(self.frameTicket)
						self.frameSingleTicket.pack(side="right",expand=True,fill="both")
						#le paso el nombre del file para que 
						#me de la lista de articulo-precio
						lista=self.dameListaArticulos(filename)
						#Coloco el frame ticket 
						self.ticket=ScrollableFrame(self.frameSingleTicket)
						self.ticket.pack(fill="both",expand=True)

						scrollFrame=self.ticket.scrollable_frame
						nombre_ticket=Label(scrollFrame,
							text="Ticket: "+filename[:-4],
							font=("Courier",24,"bold italic"))
						nombre_ticket.pack(fill="x",expand=True)
						venta_total=Label(scrollFrame,
							text="Venta: $"+str(self.dameVentaTicket(filename)),
							font=("Courier",22,"bold italic"))
						venta_total.pack(fill="x",expand=True)
						for item in lista:
							nombre=item[0]
							precio=item[1]
							linea=Frame(scrollFrame)
							linea.pack(fill="both",expand=True,padx=10,pady=10)
							lbl_nombre=Label(linea,text=nombre,font=("Serif",20))
							lbl_nombre.pack(side="left",fill="x",expand=True)
							lbl_precio=Label(linea,text="$"+str(precio),
								font=("Serif",20))
							lbl_precio.pack(side="right",fill="x",expand=True,
								padx=35)
			
					lbl_nombre=Label(frameView,text=filename,
						font=("Serif",20))
					lbl_nombre.pack(fill="x",expand=True)

					ventaTotal=self.dameVentaTicket(filename)
					lbl_total=Label(frameView,text="Total: $"+str(ventaTotal),
						font=("Serif",20))
					lbl_total.pack(fill="x",expand=True)

					btn_ver_ticket=Button(frameView,text="Ver",
						font=("Serif",22,"bold italic"),bg="#0D4702",fg="white",
						command=lambda filename=filename:verTicket(filename))

					btn_ver_ticket.pack()

				single_view()

				
		else:
			frameView=Frame(frameScroll,relief=SUNKEN,bd=3)
			frameView.config(bg="#f22")
			frameView.pack(padx=5,pady=5,fill="both",expand=True)
			lbl_aviso=Label(frameView,text="No hay tickets")
			lbl_aviso.pack()		


	def tiempoTicket(self):
		self.frameTiempo=Frame(self.frame)

		self.fechaSistema=Label(self.frameTiempo,text=str(self.fecha),
			font=("Courier",26,"bold italic"))
		self.fechaSistema.pack()
		btn_tiempo_atras=Button(self.frameTiempo,text="<==",
			font=("Serif",22,"bold italic"),
			bg="red",fg="white",command=lambda:self.saltar(-1))
		btn_tiempo_atras.pack(side="left")

		btn_tiempó_futuro=Button(self.frameTiempo,text="==>",
			font=("Serif",22,"bold italic"),
			bg="red",fg="white",command=lambda:self.saltar(1))
		btn_tiempó_futuro.pack(side="right")

		self.frameTiempo.pack()

		
	def saltar(self,days):
		self.fecha=self.fecha+timedelta(days=days)
		self.ruta_original=os.getcwd()+'/tickets/registros/'+str(self.fecha)+'/'
		self.fechaSistema.config(text=str(self.fecha))
		self.leerArchivo()
		self.llenarScroll()
		

	


#########Manipulacion de los archivos en JSON
	def leerArchivo(self):
		try:
			self.archivo=os.listdir(self.ruta_original)	
			self.colocarVentaDiaria()
		except Exception as e:
			self.lbl_total.config(text="Total: $0")
			self.num_tickets.config(text="Numero de tickets: 0")
			self.archivo=[]
	

	def colocarVentaDiaria(self):
		total=0
		if(len(self.archivo)>0):
			for filename in self.archivo:
				ventaTotalDiaria=self.dameVentaTotalDelDia(filename)
				total=total+ventaTotalDiaria

			self.lbl_total.config(text="Total: $"+str(total))
			self.num_tickets.config(text="Numero de tickets: "+str(len(self.archivo)))

	def dameVentaTotalDelDia(self,file):
		total=0
		with open(self.ruta_original+file) as json_file:
			data = json.load(json_file)
			total=total+data['total']

		#print("Nombre Archivo: ",archivo," Total: ",total)
		return total	

	def dameVentaTicket(self,file):
		total=0
		try:
			with open(self.ruta_original+file) as json_file:
				data = json.load(json_file)
				total=data['total']
		except Exception as e:
			print("Expecion en dameVentaTicket: ",e)
			return 0

		return total		

	def dameListaArticulos(self,file):
		lista=[]
		try:
			with open(self.ruta_original+file) as json_file:
				data = json.load(json_file)
				lista=data['lista']
		except Exception as e:
			print("Expecion en dameVentaTicket: ",e)
			return lista

		return lista


	def atras(self):
		self.frame.pack_forget()
		self.ventana.frame.pack(expand=True,fill="both")	
		
		

