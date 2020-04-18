import requests
url="https://www.epicurious.com/search/tofu%20chilli"
url="https://en.wikipedia.org/wiki/Main_Page"
response=requests.get(url)
# 200 es OK el resto ex 404 not found
print(response)
# contenido de la respuesta, en este caso la web
#utf-8 en principio sobra es por defecto
respuesta=response.content

respuesta=response.content.decode('utf-8')
busqueda='Did you know'
#busca el texto dentro de lo que ha devuelto la pagina
print(respuesta.find(busqueda))
