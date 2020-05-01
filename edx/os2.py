import os
camino=os.getcwd()

#carpetas camino absoluto de todas las carpetas en camino recuurente
#dir lista con las subcarpetas de cada carpeta
#files son lods ficheros de cada carpeta topsown oeden inverso
for carpetas,dire,files in os.walk(camino, topdown=False):
	print(carpetas)
	print(dire)
	for a in files:
		print('    ',a)