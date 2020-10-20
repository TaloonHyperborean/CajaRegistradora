from tkinter import *
from BD_productos.bd_promotores import bd_promotores
import hashlib

#Valida y verifica que el Qr sea correcto.
class ValidarPromocion:
	def __init__(self,root,pantallaPago):
		self.pantallaPago=pantallaPago
		self.root=root
		self.frame=Frame(root)
		self.frame.config(bg="#13012D")
		self.codigo=StringVar()
		self.password=StringVar()
		self.paquetes=["Paquete 1","Paquete 2","Paquete 3","Lifting Europeo"]
		self.letrero=Label(self.frame,font=("Courier",24,"bold italic"),fg="white")
		self.crearFrameInProm()

	def crearFrameInProm(self):
		self.root.geometry("1000x400")
		self.crearBotonAtras()
		lbl_cod=Label(self.frame,text="Ingresa el codigo: ",
			font=("Serif",30,"bold italic"),bg="#13012D",fg="white")
		lbl_cod.pack(fill="x",padx=5,pady=5)

		entry=Entry(self.frame,textvariable=self.codigo,
			font=("Serif",30,"bold italic"),justify="center")
		entry.pack(fill="both",padx=20,pady=5)


		lbl_pass=Label(self.frame,text="Ingresa clave: ",
			font=("Serif",25,"bold italic"),bg="#13012D",fg="white")
		lbl_pass.pack(fill="x",pady=50)

		entry_pass=Entry(self.frame,textvariable=self.password,
			font=("Serif",30,"bold italic"),show="*",justify="center")
		entry_pass.pack(fill="both",padx=20,pady=5)


		btn=Button(self.frame,text="Probar",
			font=("Serif",30,"bold italic"),bg="#808000",fg="white",
			command=lambda:self.verificarCodigo_v2(),anchor="center")
		btn.pack(fill="both",padx=20,pady=50)


	def verificarCodigo_v2(self):
		bd=bd_promotores()
		lista=bd.leerTodo()	
		codigoHash=self.codigo.get()

		for paquete in self.paquetes:
			for promotor in lista:
				nombrePromotor=promotor[1]
				resultadoHash=self.calcularHash(nombrePromotor,paquete)

				for hashLocal in resultadoHash:
					if(hashLocal[:5]==codigoHash):
						print("Cupon valido")
						self.crearLetrero("Cupon valido","#0AA208")
						return
						break


		self.crearLetrero("Cupon invalido","#C40000")				
			
					



	def calcularHash(self,nombrePromotor,paquete):
		listaHash=[]
		for i in range(0,50):
			guess=f'{nombrePromotor}{self.password.get()}{paquete}{i}'.encode()
			guess_hash=hashlib.sha256()
			guess_hash.update(guess)
			resultado=guess_hash.hexdigest()
			listaHash.append(resultado)

		return listaHash


		
	def crearLetrero(self,texto,color):				
		self.letrero.config(bg=color,text=texto)
		self.letrero.pack(fill="both")


	def crearBotonAtras(self):
		boton=Button(self.frame,text="Atras",font=("Courier",20,"bold italic"),
			bg="red",fg="white",
			command=lambda:self.atras())
		boton.pack(side="left",anchor="s",padx=5,pady=5)	

	def atras(self):
		self.codigo.set("")
		self.password.set("")
		self.frame.pack_forget()
		self.root.geometry("1000x700")
		self.pantallaPago.frame.pack(fill="both",expand=True)
		self.letrero.pack_forget()
