import numpy as np
import matplotlib.pyplot as plt
##ojo inicio fin que son log10
a=np.logspace(-1,1,20)

b=a**2
d=a**0.5
c=a**1.5

##plt.axis([-0.5,10.5,-5,105])
plt.loglog(a,b,"bo-",linewidth=2,markersize=4, label="first")
plt.loglog(a,c,"rs-",linewidth=2,markersize=4, label="second")
plt.loglog(a,d,"gd-",linewidth=2,markersize=4, label="tercero")
plt.xlabel('$X$')
plt.ylabel('$Y$')
plt.legend(loc="upper left")
plt.show()
