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

for elemento in root.findall('Books'):
	print(elemento.tag,elemento.text)
   #	if elemento.tag=='Author':

   	#	print(elk/Titleag,elemento.text)

    

 

