import matplotlib.pyplot as plt
import numpy as np
Y=np.array([10,12,9,10,11,12,15,8,9,10])
X=[1,2,3,4,5,6,7,8,9,10]
 
fig, axes = plt.subplots(facecolor="#e6daa6",nrows=2, ncols=2,figsize=(11, 8))

axes[0,0].plot(X,Y)
axes[0][0].axhline(y=Y[0],linewidth=2,color='k')
axes[0][0].axhline(y=15,linewidth=2,color='k',xmin=0.25,xmax=0.75,linestyle='dashed')
axes[0][0].axvline(x=3,linewidth=2,color='k',alpha=0.3,linestyle=':')
axes[0][0].fill_between(X,Y[0],Y,where=(Y >= Y[0]),interpolate=True,facecolor='g',alpha=0.3)
axes[0][0].fill_between(X,Y[0],Y,where=(Y<=Y[0]),interpolate=True,facecolor='r',alpha=0.3)
axes[0][0].grid()
plt.show()