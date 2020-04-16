import numpy as np
import cx_Oracle
import matplotlib.pyplot as plt


horas=[7,8,9,10,11,12,13,14,15,16,17,18]
colores=['ro-','bo-','gx-','yo--']
d_years={}

SQLACT="select ejercicio, num_7,num_8,num_9,num_10,num_11,num_12,num_13,num_14,num_15,num_16,num_17,num_18 from talba_hora where ejercicio=to_number(to_char(sysdate,'YYYY'))"
SQLANT="select EJERCICIO,num_7,num_8,num_9,num_10,num_11,num_12,num_13,num_14,num_15,num_16,num_17,num_18 from talba_hora where ejercicio BETWEEN to_number(to_char(sysdate,'YYYY')) - 4" \
		" AND to_number(to_char(sysdate,'YYYY')) -1 ORDER BY EJERCICIO"

connection = cx_Oracle.connect('iturria1/iturria@linux')
 
cursor = connection.cursor()

cursor.execute(SQLACT)
for row in cursor:
	listaact=row[1:]
	#d_years[row[0]]=sum(listaact)
	

cursor.execute(SQLANT)
#fig=plt.figure(facecolor="black",edgecolor="blue",linewidth=2.0)

#fig size tamaño de la ventana
fig, axes = plt.subplots(facecolor="#d6fffa",nrows=2, ncols=2,figsize=(11, 8))
#ajuste de los graficos a la ventana
fig.subplots_adjust(top=0.98)
fig.subplots_adjust(left=0.06)




fig.canvas.set_window_title('Número de albaranes')

i_color=0
#axes[0][0].set_title("Número de albaranes")
#axes[0][0].set_xlabel('$Hora$')
#axes[0][0].set_ylabel('$numero$')
axes[0][0].set_facecolor('xkcd:grey')
axes[0][0].grid(color='#040273', alpha=0.5, linestyle='dashed', linewidth=0.5)

#axes[0][1].set_title("albaranes x hora")
#axes[0][1].set_xlabel('$Hora$')
#axes[0][1].set_ylabel('$numero$')
axes[0][1].set_facecolor('xkcd:light grey')
axes[0][1].grid(color='#040273', alpha=0.5, linestyle='dashed', linewidth=0.5)


for row in cursor:
	d_years[row[0]]=sum(row[1:])
	axes[0][0].plot(np.linspace(7,18,12),row[1:],colores[i_color],linewidth=2,markersize=4,label=row[0])
	axes[0][0].legend(loc=0,prop={'size': 8})
	i_color+=1
	if i_color > 3:
		i_color=0
 

axes[0][1].plot(np.linspace(7,18,12),listaact,"ro-",linewidth=2,markersize=4,label="2020")
axes[0][1].legend(loc=0,prop={'size': 8})

print(d_years)
lista_years=list()
lista_total=list()
for y in sorted(d_years.keys()):
	lista_years.append(y)
	lista_total.append(d_years[y])

print (lista_years)
print(lista_total)

#axes[1][0].set_title("albaranes x año")
axes[1][0].set_xlabel('$año$')
#axes[1][0].set_ylabel('$numero$')
axes[1][0].set_facecolor('xkcd:light grey')
axes[1][0].grid(color='#040273', alpha=0.5, linestyle='dashed', linewidth=0.5)

#cambiar 2016 2019 y 2020 por variables
axes[1][0].plot(np.linspace(min(d_years.keys()),max(d_years.keys()),max(d_years.keys()) - min(d_years.keys()) + 1),lista_total,"ro-",linewidth=2,markersize=4)


cursor.close()
connection.close()

plt.show()
  


