import numpy as np
import matplotlib.pyplot as plt


x = np.linspace(0, 5, 10)
y = x ** 2



fig, axes = plt.subplots(nrows=1, ncols=2)

axes[1].plot(x, y, 'r')
axes[1].plot(x, y, 'r')
axes[1].set_xlabel('x')
axes[1].set_ylabel('y')
axes[1].set_title('title')

axes[0].plot(x, y, 'r')
axes[0].plot(x, y, 'r')
axes[0].set_xlabel('x')
axes[0].set_ylabel('y')
axes[0].set_title('titulo')



plt.show()