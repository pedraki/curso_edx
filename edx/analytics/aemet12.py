import os
import json
import matplotlib.pyplot as plt

cur_dir=os.getcwd()
dic_maximas=dict()
dic_minimas=dict()
lista1=[1,2,3]
lista2=[2,2,2]

with open(cur_dir+'\\prediccion.txt','r') as fichero:
	Py_dato=json.load(fichero)

#print (Py_dato[0].keys())
poblacion=Py_dato[0]['nombre']

#print (type(Py_dato[0]['prediccion']['dia']))
#print (len(Py_dato[0]['prediccion']['dia']))

for ele in Py_dato[0]['prediccion']['dia']:
	#print(ele.keys())
	dic_maximas[ele['fecha'][0:10]]=ele['temperatura']['maxima']
	dic_minimas[ele['fecha'][0:10]]=ele['temperatura']['minima']

fig, axes = plt.subplots(facecolor="#d6fffa",nrows=1, ncols=1,figsize=(11, 8))
fig.canvas.set_window_title('temperaturas')
axes.set_title("Max y min en " + poblacion)
axes.plot(list(dic_maximas.keys()),list(dic_maximas.values()),"ro-",linewidth=2,markersize=4,label="maxima")
axes.plot(list(dic_minimas.keys()),list(dic_minimas.values()),"bo-",linewidth=2,markersize=4,label="minima")
axes.legend(loc=0,prop={'size': 8})
axes.grid(color='#040273', alpha=0.5, linestyle='dashed', linewidth=0.5)
plt.show()

