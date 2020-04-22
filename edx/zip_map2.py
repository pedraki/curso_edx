lista=[2,3,3,5]

nlista=[val*2 for val in lista]
print (nlista)
#equivalente a 
nlista2=[*map(lambda val:val*2,lista)]
print (nlista2 )

#solo los pares 
nlista3=[val for val in lista if val%2==0 ]
print(nlista3 )
# equivalente con filter
nlista4=[*filter(lambda v: v%2==0,lista)]
print(nlista4)


