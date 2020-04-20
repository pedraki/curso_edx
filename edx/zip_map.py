def mayu(lk_ele):
	return lk_ele.upper()



number_list = [1, 2, 3,4]
str_list = ['one', 'two', 'three']
str_cap=list() 
n_list=[1,2,3,4,5,6,7]
#devuelve un iterador
a=zip(number_list,str_list)
 
print(list(a))

for x,y in a:
	print(x,y)
# con * devuelve lista , sin devuelve un iterador 
str_cap=[*map(mayu,str_list)]
print(str_cap)

str_cap2=[*map(lambda value:value.upper(),str_list)]
print(str_cap2)

#impar=filter(lambda numero:numero%2!=0,n_list)
impar=[*filter(lambda numero:numero%2!=0,n_list)]
print(impar )

for pal in  filter(lambda st:'o' in st,str_list):
	print (pal)



