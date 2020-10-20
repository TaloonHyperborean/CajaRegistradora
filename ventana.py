from tkinter import *
from PIL import ImageTk
import PIL.Image
from BD_productos.bd_promotores import bd_promotores
from promos.validar_promocion import ValidarPromocion
from promos.nuevo_promotor import nuevoPromotor
from tickets.ObjetoTicket import Ticket
from promos.ver_promotores import verPromotores
from modo_caja.cajaRegistradora import modoCaja
from datetime import date
import Constantes


class ventana():
	def __init__(self,root):
		self.root=root
		self.frame=Frame(root)
		self.frame.config(bg="#5D0210")
		self.modoCaja=modoCaja(root,self)
			
		self.bd_promotores=bd_promotores()
		self.nuevoProm=nuevoPromotor(self,root)
		
		self.verPromotores=verPromotores(root,self)

		self.ticket=Ticket(root,self)
		self.ticket.mainFrameTicket()

		

	def menuPrincipal(self):
		frameArriba=Frame(self.frame,bg="black")
		frameArriba.pack(expand=True,fill="both")

		frameMedio=Frame(self.frame,bg="black")
		frameMedio.pack(expand=True,fill="both")

		frameAbajo=Frame(self.frame,bg="black")
		frameAbajo.pack(expand=True,fill="both")

		def definirArriba():
			lbl_taloon=Label(frameArriba,text="Taloon",bg="black",fg="#DBDDDA",
				font=("Courier",14,"bold italic"))
			lbl_taloon.pack(side="left",expand=True,
				fill="both",padx=3,pady=3)

			boton_salir=Button(frameArriba,text="Salir",
				command=lambda:self.salir())
			boton_salir.config(bg="red",
				fg="white",font=("Serif",20,"bold italic"))
			boton_salir.pack(side="left",expand=False,
				fill="both",padx=10,pady=10)

		def definirMedio():
			boton_caja_registradora=Button(frameMedio,text="Modo caja",
				command=lambda:self.modalidadCaja())
			boton_caja_registradora.config(bg="#01836A",
				fg="white",font=("Serif",25,"bold italic"))
			boton_caja_registradora.pack(side="left",expand=True,
				fill="both",padx=3,pady=3)

		def definirAbajo():
			btn_nuevo_promotor=Button(frameAbajo,text="Nuevo \n promotor",
				command=lambda:self.nuevoPromotor())
			btn_nuevo_promotor.config(bg="#043501",
				fg="white",font=("Serif",24,"bold italic"))
			btn_nuevo_promotor.pack(side="left",expand=False,fill="both",padx=1,pady=1)

			btn_ver_promotores=Button(frameAbajo,text="Ver \n promotores",
				command=lambda:self.frameVerProms())
			btn_ver_promotores.config(bg="#960385",
				fg="white",font=("Serif",24,"bold italic"))
			btn_ver_promotores.pack(side="left",expand=True,fill="both",padx=1,pady=1)

			btn_ver_ticket=Button(frameAbajo,text="Boton \nver Tickets",
				command=lambda:self.verTickets())
			btn_ver_ticket.config(bg="#D89000",
				fg="white",font=("Serif",24,"bold italic"))
			btn_ver_ticket.pack(side="left",expand=True,fill="both",padx=1,pady=1)

		definirArriba()
		definirMedio()
		definirAbajo()	


	def verTickets(self):
		self.ticket.frame.pack(fill="both",expand=True)
		self.frame.pack_forget()





	def nuevoPromotor(self):
		self.nuevoProm.frame.pack(fill="both",expand=True)
		self.frame.pack_forget()
		
	def modalidadCaja(self):
		self.modoCaja.frame.pack(side="left",fill="both",expand=True)

		self.frame.pack_forget()	
	

	def crearNuevaCuenta(self):
		obj_cuenta={
			"lista":[],
			"fecha":date.today(),
			"total":0
		}
		self.cuentas.append(obj_cuenta)

				

	def frameVerProms(self):
		self.verPromotores.frame.pack(fill="both",expand=True)
		self.frame.pack_forget()

	def verProductos(self):
		self.frameEdicion.construirFrameEdicion()
		self.frameEdicion.frame.pack()
		self.frame.pack_forget()	

	def logo(self,imagen):
		lbl=Label(self.frame,image=imagen)
		lbl.grid(row=2,column=1,sticky="nsew",columnspan=3)
			
	def verContenedores(self):
		self.frame.pack_forget()
		self.frameVerContenedores.frame.pack()


	def salir(self):
		self.root.attributes('-fullscreen', False) 
	

root=Tk()
root.config(bg="#0C9203")
root.geometry("1800x1800")
#root.attributes('-fullscreen', True) 
root.title("OD")

laVentana=ventana(root)

laVentana.menuPrincipal()


laVentana.frame.pack(fill="both",expand=True)


root.mainloop()
