from tkcalendar import DateEntry
from tkinter import *
from BD_productos.bd_practica import *
from BD_productos.bd_inventario import *
from BD_productos.bd_contenedores import *

from frameContenedor import *
from frame_nuevo_producto import *
from frames.frame_promocion import *
from frames.frame_edicion_producto import *
from frames.frame_ver_contenedores import *
from frames.frame_seguridad import *
from frames.modo_pantalla import *
from PIL import Image,ImageTk


class ventana():
	def __init__(self,root,listaOfertas):
		self.root=root
		self.bd=bd_inventario()
		self.bd_contenedor=bd_contenedores()
		self.frame=Frame(root)
		
		self.listaOfertas=listaOfertas
		
		#obj_frame_seguridad=FRAME_SEGURIDAD(root,self.bd_contenedor,listaOfertas)

		self.obj_modo_pantalla=MODO_PANTALLA(root,self.frame,listaOfertas,self.bd_contenedor,self.bd)

		objetoFrame=FRAME_CONTENEDOR(root,self.frame)

		frame_edicion_obj=FRAME_EDICION_PRODUCTO(root,self.bd,self.frame)

		objetoFrameNuevoProducto=FRAME_NP(root)

		frameFormulaPromocion=FRAME_PROMOCION(root)

		self.obj_frame_ver_contenedor=FRAME_VER_CONTENEDORES(root,self.bd_contenedor,self.bd,self.frame,listaOfertas)

		self.frameEdicion=frame_edicion_obj.dameFrame(root)

		self.frameVerContenedores=self.obj_frame_ver_contenedor.dameFrame()

		self.frameNuevoProducto=objetoFrameNuevoProducto.dame_frame_np()

		self.frameNuevoContenedor=objetoFrame.dameFrame()
		self.framePromocion=frameFormulaPromocion.dameFrame()
		self.visible2=False
		self.visible3=False
		self.visible4=False


	def framePrincipal(self):
		print("Guarda algo en Git!")
		self.frame.grid(row=0, column=0, sticky=N+S+E+W)
		self.frame.config(bg="#B77C1D")
		Grid.rowconfigure(self.frame, 7, weight=1)
		Grid.columnconfigure(self.frame, 0, weight=1)

		return self.frame


	def pantallaPrincipal(self):
		self.frame.pack()
		self.frameEdicion.pack_forget()


	def modoPantalla(self):
		self.root.attributes('-fullscreen',True)
		frameMP=self.obj_modo_pantalla.dameFrame()
		#frameMP.pack(side="left",anchor="n")
		#frameMP.pack(fill="x")
		frameMP.pack(fill="both",expand=True)
		#frameMP.pack(fill="y",expand=True)
		self.frame.pack_forget()

		for item in self.listaOfertas:
			print(item.dame())


	def verProductos(self):
		self.bd.conexionBBDD()
		print("Ver productos")

		self.frameEdicion.pack()

		#self.boton_atras.pack()
		self.frame.pack_forget()	


	def verContenedores(self):
		self.bd.conexionBBDD()
		self.bd_contenedor.conexionBBDD()
		#self.bd_contenedor.conexionBBDD()
		self.frame.pack_forget()
		self.frameVerContenedores.pack()


	def mostar_panel_1(self):
	
		if(self.visible2):
			self.visible2=False
			self.frameNuevoProducto.pack_forget()
			
		else:
			self.visible2=True
			self.frameNuevoProducto.pack()


	def mostar_panel_2(self):
		self.frame.pack_forget()
		self.frameNuevoContenedor.pack()
		'''if(self.visible3):
			self.visible3=False
			self.frameNuevoContenedor.pack_forget()
		else:
			self.visible3=True
			self.frameNuevoContenedor.pack()'''

	def mostrar_panel_3(self):

		if(self.visible4):
			self.visible4=False
			self.framePromocion.pack_forget()
		else:
			self.visible4=True
			self.framePromocion.pack()				
	

listaOfertas=[]
root=Tk()
root.config(bg="#0C9203")
#root.geometry("1000x700")
root.title("Starbucks OD")
root.iconbitmap("cafe_icono.ico")
imagen=PhotoImage(file="logo_peque.png")

Grid.rowconfigure(root, 0, weight=1)
Grid.columnconfigure(root, 0, weight=1)

laVentana=ventana(root,listaOfertas)

frame=laVentana.framePrincipal()
frame.pack()
#w = Scrollbar (root,orient=HORIZONTAL)
#w.pack(side=RIGHT, fill=Y)


boton_ver_productos=Button(frame,text="Ver \n productos",command=laVentana.verProductos)
boton_ver_productos.config(bg="green",fg="white",font=("Serif",22))
boton_ver_productos.grid(row=0,column=0,sticky=N+S+E+W)


boton_ingresa_producto=Button(frame,text="Ingresar nuevo \n producto",command=lambda:laVentana.mostar_panel_1())
boton_ingresa_producto.config(bg="green",fg="white",padx=5,pady=5,font=("Serif",22))
#btn.bind('<Button-1>',mostar_panel_1)
boton_ingresa_producto.grid(row=0,column=1,sticky=N+S+E+W)#,padx=10,pady=10)

boton_ver_contenedores=Button(frame,text="Ver \n contenedores",command=laVentana.verContenedores)
boton_ver_contenedores.config(bg="green",fg="white",font=("Serif",22))
boton_ver_contenedores.grid(row=1,column=0,sticky=N+S+E+W)


boton_nuevo_contenedor=Button(frame,text="Nuevo \n contenedor",command=lambda:laVentana.mostar_panel_2())
#btn.bind('<Button-1>',mostar_panel_1)
boton_nuevo_contenedor.grid(row=1,column=1,sticky=N+S+E+W)#padx=10,pady=10)
boton_nuevo_contenedor.config(bg="green",fg="white",font=("Serif",22))

boton_crear_promocion=Button(frame,text="Crear nueva \n promocion",command=lambda:laVentana.mostrar_panel_3())
boton_crear_promocion.config(bg="green",fg="white",font=("Serif",22))
boton_crear_promocion.grid(row=2,column=0,sticky=N+S+E+W)

boton_modo_pantalla=Button(frame,text="Modo \n pantalla",command=lambda:laVentana.modoPantalla())
boton_modo_pantalla.config(bg="green",fg="white",font=("Serif",22))
boton_modo_pantalla.grid(row=2,column=1,sticky=N+S+E+W)

canvas=Canvas(frame)
canvas.grid(row=2,column=2,sticky=N+S+E+W)
imagen=PhotoImage(file="logo_peque.png")
canvas.create_image(60,10,anchor=NW,image=imagen)


root.mainloop()
