import numpy as np
import matplotlib.pyplot as plt
a=np.linspace(0,10,20)
b=a**2
c=a**1.5
grafi=plt.figure(facecolor="grey",edgecolor="blue",linewidth=2.0)
#plt.axis([-0.5,10.5,-5,120])

axes = grafi.add_axes([0.1, 0.1, 0.8, 0.8])

#grafi.add_axes([-0.5,10.5,-5,105])
axes.plot(a,b,"bo-",linewidth=2,markersize=4, label="first")
axes.plot(a,c,"rs-",linewidth=2,markersize=4, label="second")

axes.set_xlabel('$x$')
axes.set_ylabel('y')
axes.set_title('probando figuras ');
axes.set_facecolor('xkcd:dark grey')

axes.legend(loc="upper right")
#plt.savefig("H:\git\curso_edx\edx\plot.pdf")
plt.show()
