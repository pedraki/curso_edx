import string

def encode(lk_mensaje,lk_key,lk_positions):
	tama=len(lk_positions) -1
	codificado=str()
	for letra in lk_mensaje:
		posicion=positions[letra] + lk_key
		
		if posicion > tama:
			posicion=posicion%tama -1
		
		if posicion < 0:
			posicion=tama - posicion -1
		
		for letra_c in positions:
			if positions[letra_c]==posicion:
				codificado+=letra_c
				break
	return(codificado)


alfabeto=' '
message ='hi my name is caesar'
#message='xyz'
key=3


alfabeto+=string.ascii_lowercase
positions=dict()
num=0
for letra in alfabeto:
	positions[letra]=num
	num+=1
print(positions['n'])
print("el mensae era ", message)
codificado=encode(message,key,positions)
decodificado=encode(codificado,key*-1,positions)

print("codificado es ",codificado)
print("y decodificado ", decodificado)
