#histograma simulacion de suma de 10 dados
import random
import matplotlib.pyplot as plt
import numpy as np

x=list()
for i in range(100000):
    tirada=0
    for j in range(10):
        tirada+=random.choice(range(1,7)) 
    x.append(tirada)
plt.hist(x,bins=np.linspace(9.5,60.5,51),edgecolor="black",density=True)
#plt.hist(x,bins=np.linspace(1.5,12.5,11),edgecolor="black",density=True)
plt.show()
                        
