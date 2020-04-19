
import requests
import json
import os
url = "https://opendata.aemet.es/opendata/api/prediccion/especifica/municipio/diaria/"
api_key="eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJwZWRyby5nbWVyaW5vQGdtYWlsLmNvbSIsImp0aSI6IjMwOGJmODcwLTk5NjAtNDY3Mi1iNjFkLTYzMDVkYTkxMDJlZiIsImlzcyI6IkFFTUVUIiwiaWF0IjoxNTE4NDI3MDk0LCJ1c2VySWQiOiIzMDhiZjg3MC05OTYwLTQ2NzItYjYxZC02MzA1ZGE5MTAyZWYiLCJyb2xlIjoiIn0.5sBdnsfBDQBZVJ2YgkYWIlHmJYsPkEakXqJGfwPoiJc"
municipio="20069"

url=url+municipio

cur_dir=os.getcwd()

querystring = {"api_key":api_key}

headers = {
    'cache-control': "no-cache"
    }

 
response = requests.request("GET", url, headers=headers, params=querystring)
Py_dato=json.loads(response.content.decode())

url_datos=Py_dato['datos']

response2 = requests.request("GET",url_datos)
Py_dato2=response2.json()

print(type(Py_dato2))

with open(cur_dir+"\\prediccion.txt","w") as outfile:
	json.dump(Py_dato2,outfile,indent=2)
