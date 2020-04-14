#histograma simulacion de suma de 10 dados usando numpy
import random
import matplotlib.pyplot as plt
import numpy as np
suma=list()
# num inicial, num final, tamaño del array
X=np.random.randint(1,7,(10000000,10))

##for j in X:
##    suma.append(sum(j))
##print("suma")
##print(suma)

#axis=0 suma x filas, axis=1 sumsa x cols
# sin axis suma todo el array
SumaLin= (np.sum(X,axis=1))
plt.hist(SumaLin,edgecolor="black",density=True,bins=np.linspace(9.5,60.5,51))
plt.show()
