import json

dato='[{"b":[2,4],"c":3.0,"d":"A"}] '
#dato='{"rojo":"#f00","verde":"#0f0","azul":"#00f","cyan":"#0ff"}'
Py_dato=json.loads (dato)

print(Py_dato) 
print(type(Py_dato)) 
print(Py_dato[0]['b'][0])

a=[1,2,2,2]
#convierte la lista en tipo string
Jy_dato=json.dumps(a)
print(Jy_dato)
print(type(Jy_dato))