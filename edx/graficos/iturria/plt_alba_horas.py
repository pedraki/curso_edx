import numpy as np
import cx_Oracle
import matplotlib.pyplot as plt

#horas=[7,8,9,10,11,12,13,14,15,16,17,18]
colores=['ro-','bo-','gx-','yo--','ko--']
d_years={}

SQLACT="select ejercicio,num_resto, num_7,num_8,num_9,num_10,num_11,num_12,num_13,num_14,num_15,num_16,num_17,num_18 from talba_hora where ejercicio=to_number(to_char(sysdate,'YYYY'))"

SQLANT="select EJERCICIO,num_resto,num_7,num_8,num_9,num_10,num_11,num_12,num_13,num_14,num_15,num_16,num_17,num_18 from talba_hora where ejercicio BETWEEN to_number(to_char(sysdate,'YYYY')) - 4" \
		" AND to_number(to_char(sysdate,'YYYY')) -1 ORDER BY EJERCICIO"

SQLIMP="select Ano,ENERO_venta,febrero_venta,marzo_venta,abril_venta,mayo_venta,junio_venta,julio_venta,agosto_venta,septiembre_venta,octubre_venta, noviembre_venta,diciembre_venta \
		from estad_albaranes \
		where  ano BETWEEN to_number(to_char(sysdate,'YYYY')) - 4 AND to_number(to_char(sysdate,'YYYY')) \
		 order by ano asc"

connection = cx_Oracle.connect('iturria1/iturria@linux')
cursor = connection.cursor()

cursor.execute(SQLACT)
for row in cursor:
	listaact=row[2:]
	#d_years[row[0]]=sum(listaact)
	

cursor.execute(SQLANT)
#fig=plt.figure(facecolor="black",edgecolor="blue",linewidth=2.0)
#fig size tamaño de la ventana
fig, axes = plt.subplots(facecolor="#e6daa6",nrows=2, ncols=2,figsize=(11, 8))
#ajuste de los graficos a la ventana
fig.subplots_adjust(top=0.98)
fig.subplots_adjust(left=0.06)
fig.canvas.set_window_title('Número de albaranes')
i_color=0
#axes[0][0].set_title("Número de albaranes")
#axes[0][0].set_xlabel('$Hora$')
#axes[0][0].set_ylabel('$numero$')
axes[0][0].set_facecolor('xkcd:light grey')
axes[0][0].grid(color='#040273', alpha=0.5, linestyle='dashed', linewidth=0.5)
axes[0][0].set_xlabel('albaranes x hora' ,size=8)
for row in cursor:
	d_years[row[0]]=sum(row[1:])
	axes[0][0].plot(np.linspace(7,18,12),row[2:],colores[i_color],linewidth=2,markersize=4,label=row[0])
	axes[0][0].legend(loc=0,prop={'size': 8})
	i_color+=1
	if i_color > 3:
		i_color=0
 

 #axes[0][1].set_title("albaranes x hora")
axes[0][1].set_xlabel('albaranes x hora' ,size=8)
#axes[0][1].set_ylabel('$numero$')
axes[0][1].set_facecolor('xkcd:light grey')
axes[0][1].grid(color='#040273', alpha=0.5, linestyle='dashed', linewidth=0.5)

axes[0][1].plot(np.linspace(7,18,12),listaact,"ro-",linewidth=2,markersize=4,label="2020")
axes[0][1].legend(loc=0,prop={'size': 8})

lista_years=list()
lista_total=list()
for y in sorted(d_years.keys()):
	lista_years.append(y)
	lista_total.append(d_years[y])


#axes[1][0].set_title("albaranes x año")
axes[1][0].set_xlabel('albaranes x año',size=8)
#axes[1][0].set_ylabel('$numero$')
axes[1][0].set_facecolor('xkcd:light grey')
axes[1][0].grid(color='#040273', alpha=0.5, linestyle='dashed', linewidth=0.5)

#cambiar 2016 2019 y 2020 por variables

lista_y=np.linspace(min(d_years.keys()),max(d_years.keys()),max(d_years.keys()) - min(d_years.keys()) + 1)
lista_ye=list()
for y in lista_y:
	lista_ye.append(str(int(y)))
 
max_val_y=max(lista_total)
min_val_y=min(lista_total)
#max_val_x=max(lista_ye)

#distancia=100 
# limita los valores del eje y 
axes[1][0].set_ylim(bottom=min_val_y - 500,top=max_val_y + 500)
# saca el eje en escala linear (defecto) log logaritmica
axes[1][0].set_yscale('linear')

#axes[1][0].plot(np.linspace(min(d_years.keys()),max(d_years.keys()),max(d_years.keys()) - min(d_years.keys()) + 1),lista_total,"ro-",linewidth=2,markersize=4)
axes[1][0].plot(lista_ye,lista_total,"ro-",linewidth=2,markersize=4)



for i,j in zip(lista_ye,lista_total):
	axes[1][0].annotate(j,xy=(i,j),xycoords='data',
		xytext=(10,-30), textcoords='offset points',size=8,horizontalalignment='right', verticalalignment='top',
		bbox=dict(boxstyle="round", alpha=0.3),
		arrowprops=dict(arrowstyle="wedge,tail_width=0.5", alpha=0.4));


#ax.annotate('Christmas', xy=('2012-12-25', 3850),  xycoords='data',
#             xytext=(-30, 0), textcoords='offset points',
#             size=13, ha='right', va="center",
#             bbox=dict(boxstyle="round", alpha=0.1),
#             arrowprops=dict(arrowstyle="wedge,tail_width=0.5", alpha=0.1));

meses=["ene","feb","mar","abr","may","jun","jul","ago","sep","oct","nov","dic"]


cursor.execute(SQLIMP)
for row in cursor:
	#d_years[row[0]]=sum(row[1:])
	axes[1][1].plot(meses,row[1:],colores[i_color],linewidth=2,markersize=4,label=row[0])
	axes[1][1].legend(loc=0,prop={'size': 7})
	i_color+=1
	if i_color > 4:
		i_color=0
axes[1][1].set_xlabel('importe x mes / año',size=8)
axes[1][1].set_facecolor('xkcd:light grey')
axes[1][1].grid(color='#040273', alpha=0.5, linestyle='dashed', linewidth=0.5)

cursor.close()
connection.close()

plt.show()
  


