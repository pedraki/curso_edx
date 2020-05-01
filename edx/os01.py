import os
# S.O
print(os.name)
#Variables del sistema
#diccionario
#para ver los valores
#for s in os.environ:
#	print (s)
print(os.environ['USERNAME'])
#lo mismo pero función en vez dict
#el dict puede cambiar
print(os.getenv('USERNAME'))
#direectorio actual
print(os.getcwd())

os.chdir('c:\\pedro')
print(os.getcwd())
#solo directorio lo crea en el actual, se puede poner camino completo, solo crea uno
# lo mismo para borrar, solo borra si vacio
if not os.path.exists('c:\\pedro\\pp'):
	os.mkdir('c:\\pedro\\pp')
if os.path.exists('c:\\pedro\\pp'):
	os.rmdir('c:\\pedro\\pp')
#crea varrias carpetas anidadas
#os.makedirs('c:\\pedro\\pp\\pp1')
#os.remove(fichero) borra fichero
#solo directorios vacios
#os.rename('c:\\pedro\\pp', 'c:\\pedro\\pp1')