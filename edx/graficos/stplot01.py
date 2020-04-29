import matplotlib.pyplot as plt

dias=[1,2,3,4,5,5,7]

dormir=  [8,7,9,7,6,9,8]
comer=   [2,1,1,1,2,3,2]
trabajar=[8,9,9,9,6,1,1]
jugar=   []
for x in range(7):
	jugar.append(24 - (dormir[x] + comer[x] + trabajar[x]))

#como es un ploligono no se pueden poner legend
#para ello creamos plots vacios
plt.plot([],[],color='m',label='trabajar',linewidth=5)
plt.plot([],[],color='c',label='comer',linewidth=5)
plt.plot([],[],color='k',label='jugar',linewidth=5)
plt.plot([],[],color='r',label='dormir',linewidth=5)
plt.stackplot(dias,trabajar,comer,jugar,dormir,colors=['m','c','k','r'])
plt.legend()
plt.show()


