a=["pooja","lina","liza"]
b=["x","y","z"]
i=0
m=[]
while i<len(a):
	j=0
	while j<len(b):
		c=a[i]+b[j]
		m.append(c)
		break
		j=j+1
	i=i+1
print(m)