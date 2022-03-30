list=[1,2,3,4,6,7,8,9]
i=0
n=[]
m=[]
while i<len(list):
	k=1
	c=0
	while k<=list[i]:
		if list[i]%k==0:
			c=c+1
		k=k+1
		b=list[i]
	if c==2:
		n.append(b)
	else:
		m.append(b)
	i=i+1
print(n,"prime") 
print(m,"not prime")