import numpy as np
import cx_Oracle
import matplotlib.pyplot as plt

def valores_comunes(grafico,titulox):
	grafico.set_facecolor('xkcd:light grey')
	grafico.grid(color='#040273', alpha=0.5, linestyle='dashed', linewidth=0.5)
	grafico.legend(loc=0,prop={'size': 7})
	grafico.set_xlabel(titulox ,size=8)

SQLVTAS="select ano,total_venta,total_compra, margen_venta,resultado  \
	    from vestad_albaranes \
	    where ano BETWEEN to_number(to_char(sysdate,'YYYY')) - 14 AND to_number(to_char(sysdate,'YYYY')) -1 \
        order by ano asc"
SQLEXPO="select ano,total_venta_expo  \
	    from vestad_albaranes_expo \
	    where ano BETWEEN to_number(to_char(sysdate,'YYYY')) - 14 AND to_number(to_char(sysdate,'YYYY')) -1 \
        order by ano asc"

SQLMES="select enero_venta,febrero_venta,marzo_venta,abril_venta,mayo_venta,junio_venta,julio_venta,agosto_venta,septiembre_venta,octubre_venta, noviembre_venta,diciembre_venta, \
		enero_venta_ex,febrero_venta_ex,marzo_venta_ex,abril_venta_ex,mayo_venta_ex,junio_venta_ex, \
		julio_venta_ex,agosto_venta_ex,septiembre_venta_ex,octubre_venta_ex, noviembre_venta_ex,diciembre_venta_ex \
		from vestad_albaranes_expo \
		where  ano = to_number(to_char(sysdate,'YYYY'))"

d_years_v={}
d_years_c={}
d_years_m={}
d_years_r={}

d_years_e={}

connection = cx_Oracle.connect('iturria1/iturria@linux')
cursor = connection.cursor()

cursor.execute(SQLVTAS)
meses=["ene","feb","mar","abr","may","jun","jul","ago","sep","oct","nov","dic"]
#meses=[1,2,3,4,5,6,7,8,9,10,11,12]

for row in cursor:
	d_years_v[row[0]]=(row[1])
	d_years_c[row[0]]=(row[2])
	d_years_m[row[0]]=(row[3])
	d_years_r[row[0]]=(row[4])

cursor.execute(SQLEXPO)
for row in cursor:
	d_years_e[row[0]]=(row[1])


lista_expo=list()
cursor.execute(SQLMES)
for row in cursor:
	lista_expo=row

cursor.close()
connection.close

lista_dif_expo_act=list()
Ll=zip(lista_expo[0:12],lista_expo[12:24])
for i,j in Ll:
	if i and j != None:
		lista_dif_expo_act.append(i - j)
	else:
		lista_dif_expo_act.append(None)


lista_dif_ventas=list()
lista_dif_expo=list()
for i in d_years_v:
	lista_dif_expo.append(d_years_v[i] - d_years_e[i])
	lista_dif_ventas.append(d_years_v[i] - d_years_c[i])




lista_y=np.linspace(min(d_years_v.keys()),max(d_years_v.keys()),max(d_years_v.keys()) - min(d_years_v.keys()) + 1)
lista_ye=list()
for y in lista_y:
	lista_ye.append(str(int(y))[2:4])



fig, axes = plt.subplots(facecolor="#e6daa6",nrows=2, ncols=2,figsize=(11, 8))
#ajuste de los graficos a la ventana
fig.subplots_adjust(top=0.98)
fig.subplots_adjust(left=0.06)
fig.canvas.set_window_title('Estadisticas albaranes')

#Grafico 1 compras/ventas de albaranes
axes[0][0].plot(lista_ye,list(d_years_v.values()),"go-",linewidth=2,markersize=4,label='Ventas')
axes[0][0].plot(lista_ye,list(d_years_c.values()),"ro-",linewidth=2,markersize=4,label='Compras')
axes[0][0].plot(lista_ye,lista_dif_ventas,"ko--",linewidth=2,markersize=4,label='dif')
axes[0][0].fill_between(lista_ye,list(d_years_c.values()),list(d_years_v.values()),alpha=0.2)
valores_comunes(axes[0][0],'Ventas / Compras (millones euros)')
#grafico 2 evolucion margen
axes[0][1].plot(lista_ye,list(d_years_m.values()),"bo-",linewidth=2,markersize=4,label='Margen')
valores_comunes(axes[0][1],'Margen sobre ventas')
#grafico 3 ventas expo
axes[1][0].plot(lista_ye,list(d_years_v.values()),"go-",linewidth=2,markersize=4,label='Total')
axes[1][0].plot(lista_ye,list(d_years_e.values()),"bo-",linewidth=2,markersize=4,label='Expo')
axes[1][0].plot(lista_ye,lista_dif_expo,"ko--",linewidth=2,markersize=4,label='dif')
axes[1][0].fill_between(lista_ye,list(d_years_e.values()),list(d_years_v.values()),alpha=0.2)
valores_comunes(axes[1][0],'expo VS total (millones euros)')
#grafico 4 ventas expo vs total mensual actual
axes[1][1].plot(meses,lista_expo[0:12],"go-",linewidth=2,markersize=4,label='Total')
axes[1][1].plot(meses,lista_expo[12:],"bo-",linewidth=2,markersize=4,label='Expo')
axes[1][1].plot(meses,lista_dif_expo_act,"ko--",linewidth=2,markersize=4,label='dif')
#axes[1][1].fill_between(meses,lista_expo[12:15],lista_expo[0:3],alpha=0.2)
valores_comunes(axes[1][1],'expo VS total (miles de euros), actual')

plt.show()