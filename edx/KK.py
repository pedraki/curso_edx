import numpy as np
X=np.zeros((3,3))

X[0][2]=1
X[1][1]=1
X[2][0]=1


print(X)
#fliplr= flip(X, axis=1)
#print(np.fliplr(X))
if np.all(np.diag(X,0)==1):
	print("diagonal")

if np.all(np.diag(np.fliplr(X),0)==1):
	print ("diagonal inversa")

filas=np.all(X==1,axis=1)
colus=np.all(X==1,axis=0)

if np.any(colus==True) or np.any(filas==True):
	print("gano")
print ("filas", filas)
print ("columas",colus)



#for x in range(3):

#	print("Columna")
#	print (X[:,x])
#	print(np.all(X[:,x])==0)

#	print("fila")
#	print (X[x])
#	print(np.all(X[x])==0)

#print(np.all(X)==0)
 