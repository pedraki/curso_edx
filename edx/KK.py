number_list = [1, 2, 3,4]
str_list = ['one', 'two', 'three']

a=zip(number_list,str_list)
#print(list(a))

for x,y in a:
	print(x,y)