#Random walk
# se empieza del punto 0,0 y casa paso es aleatorio
# se calcula XN como XN -1 + Desplazamiento
import random
import matplotlib.pyplot as plt
import numpy as np
import time
inicio=time.process_time()

#XY0 posicion 0,0
XY0=np.zeros((2,1))
#Desp son los desplazamientos aleatorios
#en el eje X e Y siguiendo distribucion normal
Desp=np.random.normal(0,1,(2,1000))
 
#suma acumulativa
#Posicion es la suma acumulutava de los desplazamientos             
Posicion=np.cumsum(Desp,axis=1)
 
#le añadimos el punto inicial 0,0
Posicion=np.concatenate((XY0,Posicion),axis=1)
 
plt.plot(Posicion[0],Posicion[1],"bo-")
 
plt.show()
