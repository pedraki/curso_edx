import numpy as np
import matplotlib.pyplot as plt
# if using a Jupyter notebook, include:


x = np.linspace(0, 10)
fig, ax = plt.subplots()
plt.xkcd()
#plt.style.use('ggplot')
plt.grid()

for n in range(-20,30,10):
    ax.plot(x, np.cos(x) + np.random.randn(50) + n)

ax.set_title("'fivethirtyeight' style")

plt.show()
