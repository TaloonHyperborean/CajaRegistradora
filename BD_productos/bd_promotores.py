from tkinter import *
from tkinter import messagebox
import sqlite3
from tkcalendar import DateEntry
from datetime import datetime


#####################################################

class bd_promotores():
	def __init__(self):
		self.conexionBBDD()

	def crear(self,name,address,fecha,codigoHash):
		 miConexion=sqlite3.connect("proms")
		 miCursor=miConexion.cursor()
		 datos=name,address,fecha,codigoHash

		 miCursor.execute("INSERT INTO PROMOTORES VALUES(NULL,?,?,?,?)",(datos))
		 miConexion.commit()
		 #messagebox.showinfo("BBDD_promotores","Registro insertado con exito")


	def leerTodo(self):
		try:
			miConexion=sqlite3.connect("proms")
			cursor=miConexion.cursor()
			cursor.execute("SELECT * FROM PROMOTORES");
			resultados=cursor.fetchall()

			return resultados
			miConexion.commit()
		except Exception as e:
			print(e)




	def actualizar(self,id_promocion,respuesta):
		 miConexion=sqlite3.connect("proms")
		 miCursor=miConexion.cursor()
		 datos=id_promocion,respuesta

		 miCursor.execute("UPDATE PROMOTORES SET ID=?,USE=?"+"WHERE ID="+str(id_promocion),(datos))
		 miConexion.commit()
		 print("Valor actualizado")
	


	def conexionBBDD(self):
	 miConexion=sqlite3.connect("proms")
	 miCursor=miConexion.cursor()

	 try:
		 miCursor.execute('''
		 CREATE TABLE PROMOTORES (
		 ID INTEGER PRIMARY KEY AUTOINCREMENT,
		 NAME VARCHAR(250),
		 ADDRESS VARCHAR(250),
		 FECHA VARCHAR(250),
		 HASHID VARCHAR(250))
		 ''')
		 messagebox.showinfo("BBDD_promotores","BBDD creada con exito")
	 except Exception as e:
	 	#messagebox.showwarning("Atencion","La base de datos ya existe")  
	 	print(e)













