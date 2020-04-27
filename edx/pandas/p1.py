import os
import pandas as pd
import matplotlib.pyplot as plt
fichero=os.path.join(os.getcwd(),'datasets\\avocado.csv')
df=pd.read_csv(fichero)
#pasamos la fecha a tipo fecha
df['Date']=pd.to_datetime(df['Date'])
df.head()
albany_df=df[df['region']=='Albany']
albany_df.set_index('Date', inplace=True)
#ordenamos por el indice en este caso la fecha
df2=albany_df.sort_index()
#albany_df.sort_index(inplace=True)

#rolling (k) crea una ventana de k elementos para calcular
#por ejemplo el promedio o la suma movil
df2['AveragePrice'].rolling(25).mean().plot()
#df2['AveragePrice'].plot()
#plt.show()
print(df2['AveragePrice'].rolling(25).mean())