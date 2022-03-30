list=[12,67,98,34]
i=0
sum=0
m=[]
while i<len(list):
	b=list[i]%10
	c=list[i]//10
	sum=b+c
	m.append(sum)
	i=i+1
print(m)