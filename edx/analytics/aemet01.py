
import requests
import json
import os

url = "https://opendata.aemet.es/opendata/api/valores/climatologicos/inventarioestaciones/todasestaciones/"

querystring = {"api_key":"eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJwZWRyby5nbWVyaW5vQGdtYWlsLmNvbSIsImp0aSI6IjMwOGJmODcwLTk5NjAtNDY3Mi1iNjFkLTYzMDVkYTkxMDJlZiIsImlzcyI6IkFFTUVUIiwiaWF0IjoxNTE4NDI3MDk0LCJ1c2VySWQiOiIzMDhiZjg3MC05OTYwLTQ2NzItYjYxZC02MzA1ZGE5MTAyZWYiLCJyb2xlIjoiIn0.5sBdnsfBDQBZVJ2YgkYWIlHmJYsPkEakXqJGfwPoiJc"}

headers = {
    'cache-control': "no-cache"
    }


cur_dir=os.getcwd()

response = requests.request("GET", url, headers=headers, params=querystring)
Py_dato=json.loads(response.content.decode())

response2= requests.request("GET", Py_dato['datos'], headers=headers, params=querystring)

# mejor usar la primera
Py_dato3=response2.json()
Py_dato2=json.loads(response2.text)

with open(cur_dir + '\\aemet1.txt', 'w') as outfile:
    json.dump(Py_dato2, outfile,indent=2)

with open(cur_dir + '\\aemet2.txt', 'w') as outfile:
    json.dump(Py_dato3, outfile)