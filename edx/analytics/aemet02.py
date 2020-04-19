
import requests
import json


with open('H:\\git\\curso_edx\\edx\\analytics\\aemet2.txt', 'r') as outfile:
    Py_dato=json.load(outfile)

#print(type(Py_dato))
#print(Py_dato)
for ele in Py_dato:
	if ele['indicativo']=="1024E":
		print(ele)
 