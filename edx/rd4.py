#histograma simulacion de suma de 10 dados
import random
import matplotlib.pyplot as plt
import numpy as np

# distribucion normal de 0 a 1 reales igual propabilidad
print(np.random.random())
#genera lista con 5 numeros
#ojo la que no es de numpy no funciona
print(np.random.random(5))
# array 2d de 3 filas 4 col
print(np.random.random((3,4)))
#Distribuion normal, media, desviacion stad , numero elementos
print("distribucion normal")
print(np.random.normal(0,1,(2,3))) 
                        
