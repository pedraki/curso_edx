import numpy as np
import matplotlib.pyplot as plt
a=np.linspace(0,10,20)
b=a**2
c=a**1.5
plt.axis([-0.5,10.5,-5,105])
plt.plot(a,b,"bo-",linewidth=2,markersize=4, label="first")
plt.plot(a,c,"rs-",linewidth=2,markersize=4, label="second")
plt.xlabel('$X$')
plt.ylabel('$Y$')
plt.legend(loc="upper right")
plt.savefig("h:\python\edx\plot.pdf")
plt.show()
