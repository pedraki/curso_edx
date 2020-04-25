from  lxml import etree
import os

cur_dir=os.getcwd()
fichero=cur_dir + '\\prueba.xml'

#pasa lee el fichero XML
Fxml=etree.parse(fichero)
#print(type(Fxml))
#lo pasa a string para tratarlo
FSxml=etree.tostring(Fxml,pretty_print=True).decode()
root=etree.XML(FSxml)
#print(root.tag)
elemento1=etree.tostring(root,pretty_print=True).decode()
## root.iter() es un iterador como range
for elemento in root.iter():
   print(elemento)