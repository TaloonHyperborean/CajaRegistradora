import pyqrcode
import os


class QrClass:
	def __init__(self,promotor,hashQR):
		#
		self.Promotor=promotor
		self.hashPromotor=self.Promotor[4]
		self.hashQR=hashQR

	def codigo_caducidad(self,fechaLimite):
		codigoQrText=self.hashQR+":"+self.hashPromotor+":"+str(fechaLimite)		
		self.big_code = pyqrcode.create(codigoQrText, error='L', version=7, mode='binary')

		self.crearCaminoArchivo()

		archivo='promos/codigos/'+self.hashPromotor+'/'+self.hashQR[:5]+".png"
		
		self.big_code.png(archivo, 
			scale=2, module_color=[0, 0, 0, 0], background=[0xff, 0xff, 0xff])

	def codigi_edicionLimitada(self):
		codigoQrText=self.hashCodigo[:5]+":"+promotor
		self.big_code = pyqrcode.create(codigoQrText, error='L', version=5, mode='binary')	


	def crearCaminoArchivo(self):
		#En Promotor[4] se encuentra el hash del promotor
		camino_archivo='promos/codigos/'+self.Promotor[4]+'/'
		try:
			#
		    os.makedirs(camino_archivo)
		except OSError as e:
		    print("Ya existe ruta")

	def mostrarCodigo(self):
		#
		self.big_code.show()