import matplotlib.pyplot as plt

dias=['L','M','X','J','V','S','D']
colores=['m','c','k','r']

dormir=  [8,7,9,7,6,9,8]
comer=   [2,1,1,1,2,3,2]
trabajar=[8,9,9,9,6,1,1]
jugar=   []
actividades=['trabajar','comer','jugar','dormir']
dias_d=dict()
for x in range(7):
	jugar.append(24 - (dormir[x] + comer[x] + trabajar[x]))
	dias_d[dias[x]] = [trabajar[x],comer[x],jugar[x],dormir[x]]

fig, axes = plt.subplots(facecolor="#e6daa6",nrows=2, ncols=4,figsize=(11, 8))


axes[0][0].pie(dias_d['L'],labels=actividades,startangle=90)
axes[0][0].set_title('lunes',color='r')
axes[0][1].pie(dias_d['M'],labels=actividades,shadow=True)
#explode cada numero es de un quesito de la lista
#radius tamaño del queso deafult 1??
axes[0][2].pie(dias_d['X'],labels=actividades,explode=(0,0,0.1,0),shadow=True,radius=1.2)
axes[0][3].pie(dias_d['J'],labels=actividades,autopct='%1.1f%%')
axes[1][0].pie(dias_d['V'],labels=actividades,textprops={'size': 'smaller'})
axes[1][2].pie(dias_d['S'],labels=actividades)
axes[1][2].set_title('sábado',color='r')
axes[1][3].pie(dias_d['D'],labels=actividades)
axes[1][1].pie([],[])

plt.show()


