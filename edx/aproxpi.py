import math
import random

random.seed(1) # Fixes the see of the random number generator.

def rand():
   return(random.uniform(-1.0,1.0))

rand()

def in_circle(x, origin = [0,0]):
    x1,x2=x
    o1,o2=origin
    if math.sqrt((x1-o1)**2+(x2-o2)**2) < 1:
        return True
    else:
        return False
R=1000
inside=list()
for i in range(R):
    inside.append(in_circle((rand(),rand())))

proportion=inside.count(True) / R
print(proportion)
print(proportion*4)
print ("diferencia ", math.pi - proportion * 4)
print ("diferencia ex  ", math.pi/4 - proportion)
