from  lxml import etree
import os

cur_dir=os.getcwd()
fichero=cur_dir + '\\factura.xml'

#pasa lee el fichero XML
Fxml=etree.parse(fichero)
#print(type(Fxml))
#lo pasa a string para tratarlo
FSxml=etree.tostring(Fxml,pretty_print=True).decode()
root=etree.XML(FSxml)
#print(root.tag)
elemento1=etree.tostring(root,pretty_print=True).decode()
## root.iter() es un iterador como range
# la diferencia entre .iter() y nada es que nada saca
#solo los hijos , e iter itera por todo el xml
#se puede sacar el elemento o las etiquetas con .tag
for elemento in root:
   print(elemento.tag)
   for child in elemento:
      #print(elemento)
      print('   ', child)
      for subc in child:
         print('         ' ,subc)

print('fin')
for elemento in root:
   print(elemento.tag)
   for child in elemento:
      print('   ',child.tag)

