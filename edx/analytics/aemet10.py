
import requests
import json
url = "https://opendata.aemet.es/opendata/api/prediccion/especifica/municipio/diaria/"

querystring = {"api_key":"eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJwZWRyby5nbWVyaW5vQGdtYWlsLmNvbSIsImp0aSI6IjMwOGJmODcwLTk5NjAtNDY3Mi1iNjFkLTYzMDVkYTkxMDJlZiIsImlzcyI6IkFFTUVUIiwiaWF0IjoxNTE4NDI3MDk0LCJ1c2VySWQiOiIzMDhiZjg3MC05OTYwLTQ2NzItYjYxZC02MzA1ZGE5MTAyZWYiLCJyb2xlIjoiIn0.5sBdnsfBDQBZVJ2YgkYWIlHmJYsPkEakXqJGfwPoiJc"}

headers = {
    'cache-control': "no-cache"
    }

 
response = requests.request("GET", url, headers=headers, params=querystring)
Py_dato=response.json()
