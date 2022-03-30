list=[2,3,5,4,6,7]
i=0
a=[]
b=2
while i<len(list):
	if b<len(list):
		a.append(list[i:i+b])
	i=i+b
print(a)