import os
import pandas as pd
fichero=os.path.join(os.getcwd(),'datasets\\libro1.csv')
df=pd.read_csv(fichero)
#pasamos la fecha a tipo fecha
df['fecha']=pd.to_datetime(df['fecha'])
df.head()
#albany_df=df[df['region']=='Albany']
df.set_index('fecha', inplace=True)
#albany_df['AveragePrice'].rolling(25).mean().plot()