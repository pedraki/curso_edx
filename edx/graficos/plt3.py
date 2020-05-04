import matplotlib.pyplot as plt
import numpy as np
x=np.random.normal(size=1000)
plt.style.use('seaborn-dark-palette')
#density=True saca el % de casos, si no saca
#total de casos
#bins intervalos para n intervalos hacen falta 2n+1 puntos
plt.hist(x,density=True,bins=np.linspace(-5,5,21));
#plt.hist(x );
#plt.show()
print(plt.style.available)
