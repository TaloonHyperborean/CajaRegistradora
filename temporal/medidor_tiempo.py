from timer import *

tiempo=Timer()

tiempo.start()

for i in range(0,1000000):
	r="hola"

tiempo.stop()
print(r)