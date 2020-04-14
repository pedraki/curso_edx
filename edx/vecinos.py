import random
random.seed(1)
def moving_window_average(x, n_neighbors=1):
    list_modi= list()
    n = len(x)
    width = n_neighbors*2 + 1
    for i in range(n):
        suma_vecinos=x[i]
        for posicion in range(1,n_neighbors+1 ):
            anterior=i-posicion
            posterior=i+posicion
            if posterior > n -1:
                suma_vecinos+=x[i]
            else:
                suma_vecinos+=x[posterior]

            if anterior < 0:
                suma_vecinos+=x[i]
            else:
                suma_vecinos+=x[anterior]
        suma_vecinos=suma_vecinos / width
        list_modi.append(suma_vecinos)
    return list_modi
 
def rand():
   return(random.uniform(0.0,1.0))
x=list()
y=list()
for i in range(1000):
    x.append(rand())
y.append(x)
 
for j in range(1,9):
    y.append(moving_window_average(x, j))
list_ranges=list() 
for elemento in y:
    list_ranges.append(max(elemento) - min(elemento))

print (list_ranges)

