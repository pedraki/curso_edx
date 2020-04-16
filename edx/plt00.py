import numpy as np
import matplotlib.pyplot as plt


x = np.linspace(0, 5, 10)
y = x ** 2



fig, axes = plt.subplots(nrows=1, ncols=2)
fig.canvas.set_window_title('Número de albaranes')

for ax in axes:
    ax.plot(x, y, 'r')
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_title('title')
    print("hola",ax)

plt.show()