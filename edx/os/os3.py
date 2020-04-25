import os

camino=os.getcwd()
#devuelve eel nombre de la ultima carpeta del camino 
print(os.path.basename(camino))
#devuelve la carpeta de un fichero 
print(os.path.dirname(camino+'\\pp.txt'))
#se el caminio es un directorio o un fichero
# si no existe devuelve falso
print(os.path.isdir(camino))
print(os.path.isfile(camino))
print(os.path.isdir('c:\\camino'))
#junta camino con fihero
print(os.path.join(camino,'pp.txt'))
#ojo 
lista=['c:\\','pedro','pp.txt']
print(os.path.join(*lista))
#separa la ultima subcarpeta del camino
a, b=os.path.split(camino)
print(a,b)
