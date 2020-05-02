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
 
def autopie(pct, valores):
	allvals=np.array(valores)
	absolute = int(pct/100.*np.sum(allvals))
	return "{:.1f}%\n{:d}".format(pct, absolute)

SQLEXPO="select nombre, t_numero, t_ofertado,t_venta,t_compra,t_beneficio  \
	    from VESTAD_OF_DEPEN_N11 \
	    where t_numero > 10 \
	          and ano = 2020 \
	          order by nombre "


 
d_dep_n=dict()
d_dep_o=dict()
d_dep_v=dict()
d_dep_b=dict()
 
connection = cx_Oracle.connect('iturria1/iturria@linux')
cursor = connection.cursor() 

cursor.execute(SQLEXPO)
for row in cursor:
	d_dep_n[row[0]]=(row[1])
	d_dep_o[row[0]]=(row[2])
	d_dep_v[row[0]]=(row[3])
	d_dep_b[row[0]]=(row[5]) 
    #d_dep_b[row[0]]=(row[5])


print(d_dep_n)
Lisn=np.array(list(d_dep_n.values()))
Liso=np.array(list(d_dep_o.values()))
Lisv=np.array(list(d_dep_v.values()))
Lisb=np.array(list(d_dep_b.values()))
colores1=['#fe01b1','#c44240','#137e6d','#040273']
colores2=['#ff7855', '#ffd1df','#82cbb2','#75fd63']   
	
cursor.close()
connection.close()

fig, axes = plt.subplots(facecolor="#e6daa6",nrows=2, ncols=4,figsize=(11, 8))
#ajuste de los graficos a la ventana
fig.subplots_adjust(top=0.98)
fig.subplots_adjust(left=0.06)
fig.canvas.set_window_title('Estadisticas expo')




axes[0][0].pie(Lisn ,labels=d_dep_n.keys(),
	           explode=(0,0,0.1,0),shadow=True,radius=1.08,
	           autopct=lambda pct: autopie(pct,Lisn),
	           colors=colores2,
	           textprops={'fontsize': '8'})

axes[0][0].set_title('Ofertas',color='k')

axes[0][1].pie(d_dep_o.values(),labels=d_dep_o.keys(),
	           explode=(0,0,0.1,0),shadow=True,radius=1.08,
	            autopct=lambda pct: autopie(pct,Liso),
	            colors=colores2,
	            #startangle=90,
	            textprops={'fontsize': '8'})
	           #autopct='%1.1f%%')
axes[0][1].set_title('Ofertado',color='k')

axes[0][2].pie(Lisv ,labels=d_dep_n.keys(),
	           explode=(0,0,0.1,0),shadow=True,radius=1.08,
	           autopct=lambda pct: autopie(pct,Lisv),
	           colors=colores2,
	           textprops={'fontsize': '8'})

axes[0][2].set_title('Vendido',color='k')

wedges, texts, autotexts = axes[0][3].pie(Lisb ,labels=d_dep_n.keys(),
	           explode=(0,0,0.1,0),shadow=True,radius=1.08,
	           autopct=lambda pct: autopie(pct,Lisb),
	           colors=colores2,
	           labeldistance=1.1,
	           textprops={'fontsize': '8'})
for text in texts:

    text.set_color('grey')
    text.set_size('9')
    #print(text)
for autotext in autotexts:
    #autotext.set_color('grey')  
    print(autotext)
axes[0][3].set_title('Beneficio',color='r')

	           #textprops={'fontsize': '8','color':'w'})
#plt.setp(autotexts, size=8, weight="bold")

plt.show() 