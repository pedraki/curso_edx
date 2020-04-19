import http.client

conn = http.client.HTTPSConnection("opendata.aemet.es")

headers = {
    'cache-control': "no-cache"
    }

conn.request("GET", "/opendata/api/valores/climatologicos/inventarioestaciones/todasestaciones/?api_key=eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJwZWRyby5nbWVyaW5vQGdtYWlsLmNvbSIsImp0aSI6IjMwOGJmODcwLTk5NjAtNDY3Mi1iNjFkLTYzMDVkYTkxMDJlZiIsImlzcyI6IkFFTUVUIiwiaWF0IjoxNTE4NDI3MDk0LCJ1c2VySWQiOiIzMDhiZjg3MC05OTYwLTQ2NzItYjYxZC02MzA1ZGE5MTAyZWYiLCJyb2xlIjoiIn0.5sBdnsfBDQBZVJ2YgkYWIlHmJYsPkEakXqJGfwPoiJc", headers=headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))