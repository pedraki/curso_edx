import numpy as np
import cx_Oracle
import matplotlib.pyplot as plt

def valores_comunes(grafico,titulox):
	grafico.set_facecolor('xkcd:light grey')
	grafico.grid(color='#040273', alpha=0.3, linestyle='dashed', linewidth=0.5)
	grafico.legend(loc=0,prop={'size': 7})
	grafico.set_xlabel(titulox ,size=8)


def autolabel(rects,ax):
    """Attach a text label above each bar in *rects*, displaying its height."""
    for rect in rects:
        height = rect.get_height()
        ax.annotate('{}'.format(height),
                    xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(-3, 1),  # 3 points vertical offset
                    textcoords="offset points",size=8,
                    ha='center', va='bottom')


SQLH20="select ano, nvl(num_reg_h20,0) +nvl(num_ara_h20,0) h20, \
		nvl(num_reg,0) + nvl(num_ara,0) total, \
		nvl(tot_reg_h20,0) + nvl(tot_ara_h20,0) h20_imp, \
		nvl(tot_reg,0) + nvl(tot_ara,0) tot_imp \
		from t_coci_alba \
		where ano BETWEEN to_number(to_char(sysdate,'YYYY')) - 14 AND to_number(to_char(sysdate,'YYYY'))   \
		order by ano asc"


SQLVTAS="select ano,total_venta \
	    from vestad_albaranes \
	    where ano BETWEEN to_number(to_char(sysdate,'YYYY')) - 4 AND to_number(to_char(sysdate,'YYYY')) \
        order by ano asc"

SQLEXPO="select ano,total_venta_expo  \
	    from vestad_albaranes_expo \
	    where ano BETWEEN to_number(to_char(sysdate,'YYYY')) - 4 AND to_number(to_char(sysdate,'YYYY')) \
        order by ano asc"



d_years_v={}
d_years_e={}

lista_y=list()
lista_h=list()
lista_r=list()
lista_t=list()
lista_hi=list()
lista_ri=list()
lista_ti=list()

connection = cx_Oracle.connect('iturria1/iturria@linux')
cursor = connection.cursor()

cursor.execute(SQLH20)
for row in cursor:
	lista_y.append(row[0])
	lista_h.append(row[1])
	lista_r.append(row[2] - row[1])
	lista_t.append(row[2])

	lista_hi.append(row[3])
	lista_ri.append(row[4] - row[3])
	lista_ti.append(row[4])


cursor.execute(SQLVTAS)
meses=["ene","feb","mar","abr","may","jun","jul","ago","sep","oct","nov","dic"]
#meses=[1,2,3,4,5,6,7,8,9,10,11,12]

for row in cursor:
	d_years_v[row[0]]=(row[1])


cursor.execute(SQLEXPO)
for row in cursor:
	d_years_e[row[0]]=(row[1])
	
cursor.close()
connection.close()

print(d_years_v.keys())



fig, axes = plt.subplots(facecolor="#e6daa6",nrows=1, ncols=2,figsize=(11, 8))
#ajuste de los graficos a la ventana
fig.subplots_adjust(top=0.98)
fig.subplots_adjust(left=0.06)
fig.canvas.set_window_title('Estadisticas cocinas')

#Grafico 1 cocinas nunero
lista_graph=list()
lista_graph.append(axes[0].bar(lista_y, lista_h, color = "g", width = 0.25,label='H20'))
lista_graph.append(axes[0].bar([v+0.25 for v in lista_y], lista_r, color = "#f8481c", width = 0.25,label='Resto'))
lista_graph.append(axes[0].bar([v+0.50 for v in lista_y], lista_t, color = "#1e488f", width = 0.25,label='Total'))

axes[0].set_xticks([v+0.25 for  v in lista_y])
axes[0].set_xticklabels([str(v) for v in lista_y])

valores_comunes(axes[0],'Cocinas facturadas (número)')
for grafi in lista_graph:
	autolabel(grafi,axes[0])

#grafico 2 cocinas importe
lista_graph=list()
lista_graph.append(axes[1].bar(lista_y, [round(v /1000,2) for v in lista_hi], 
	color = "g", width = 0.30,label='H20'))
lista_graph.append(axes[1].bar([v+0.30 for v in lista_y], [round(v /1000,2)  for v in lista_ri], 
	color = "#f8481c", width = 0.30,label='Resto'))
lista_graph.append(axes[1].bar([v+0.60 for v in lista_y], [round(v /1000,2) for v in lista_ti], 
	color = "#1e488f", width = 0.30,label='Total'))
 
axes[1].set_xticks([v+0.30 for  v in lista_y])
axes[1].set_xticklabels([str(v) for v in lista_y])
  
valores_comunes(axes[1],'Cocinas facturadas (importe en miles de euros)')
for grafi in lista_graph:
	autolabel(grafi,axes[1])


plt.show()