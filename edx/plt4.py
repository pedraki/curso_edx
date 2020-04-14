import matplotlib.pyplot as plt
import numpy as np
x=np.random.gamma(2,3,100000)
plt.figure()
#filas columnas,numero subgrafico
plt.subplot(3,2,1)
plt.hist(x,density=True,bins=30);
plt.subplot(322)
plt.hist(x,cumulative=True,bins=30,edgecolor="black");
plt.subplot(323)
plt.hist(x,cumulative=True,density=True,bins=30,histtype="step");
plt.subplot(324)
plt.hist(x,bins=30)
plt.subplot(325)
plt.hist(x,bins=30)
plt.show()
