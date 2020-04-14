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
 
x = [0,10,5,3,1,5]
print(sum(moving_window_average(x,1)))
    
