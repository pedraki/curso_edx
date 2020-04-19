
import requests
import json
import os

cur_dir=os.getcwd()


with open(cur_dir+'\\aemet2.txt', 'r') as outfile:
    Py_dato=json.load(outfile)

#print(type(Py_dato))
#print(Py_dato)
for ele in Py_dato:
	if ele['indicativo']=="1024E":
		print(ele)
 