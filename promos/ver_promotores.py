from BD_productos.bd_promotores import bd_promotores
from tkinter import *
from scrollClass import ScrollableFrame
from promos.nueva_prom import nuevaPromocion



class verPromotores:
	def __init__(self,root,ventana):
		self.ventana=ventana
		self.root=root
		self.frame=ScrollableFrame(root)
		#self.frameScroll.cambiarAncho(2000)
		#self.frameScroll.cambiarAltura(1200)
		self.bd=bd_promotores()
		self.Promocion=nuevaPromocion(root,self)
		self.listaPromotores=self.bd.leerTodo()
		self.construirFrameLista()

	def construirFrameLista(self):
		self.crearBtnAtras()
		for promotor in self.listaPromotores:
			self.agregarFila(promotor)
	

	def agregarFila(self,promotor):
		name=promotor[1]
		address=promotor[2]
		fecha_registro=promotor[3]
		hash_promotor=promotor[4]
		frameScroll=self.frame.scrollable_frame

		single_view=Frame(frameScroll)
		single_view.config(bg="#0A2A40",relief=SUNKEN,bd=3)
		single_view.pack(anchor="center",fill="both",expand=True,padx=3,pady=3)

		lbl=Label(single_view,text=promotor[1],
			font=("Courier",25,"bold italic"),bg="#0A2A40",fg="white")
		lbl.pack(side="left",fill="both",padx=15,pady=1,expand=True)	

		num_qrs_totales=Label(single_view,text="Capital generado:",
			font=("Courier",20,"bold italic"),bg="#0A2A40",fg="white")
		num_qrs_totales.pack(side="left",fill="both",
			padx=15,pady=1,expand=True)	

		num_qrs_totales=Label(single_view,text="Proms: ",
			font=("Courier",20,"bold italic"),bg="#0A2A40",fg="white")
		num_qrs_totales.pack(side="left",fill="both",
			padx=15,pady=1,expand=True)		

		btn_generar_qr=Button(single_view,text="Generar\nQr",
			font=("Courier",22,"bold italic"),bg="#400A0F",fg="white",
			command=lambda:self.crearNuevaPromocion(promotor))
		btn_generar_qr.pack(side="right",fill="both",
			padx=15,pady=1,expand=True)	


	def crearNuevaPromocion(self,promotor):
		self.frame.pack_forget()
		self.Promocion.Promotor=promotor
		self.Promocion.frame.pack(fill="both",expand=True)	

	


	def crearBtnAtras(self):
		def atras():
			self.frame.pack_forget()
			self.ventana.frame.pack(expand=True,fill="both")

		btn_atras=Button(self.frame,text="Atras",bg="red",fg="white",
			command=lambda:atras())
		btn_atras.pack(side="right",anchor="n",padx=5,pady=5)		