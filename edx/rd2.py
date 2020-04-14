#histograma simulacion de un dado
import random
import matplotlib.pyplot as plt
import numpy as np

x=list()
for i in range(1000000):
    x.append(random.choice(range(1,7)))
##    x.append(random.choice([1,2,3,4,5,6]))
plt.hist(x,bins=np.linspace(0.5,6.5,7),edgecolor="black",density=True)

plt.show()
                        
