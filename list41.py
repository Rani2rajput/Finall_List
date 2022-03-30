a="sai"
b=""
i=1
while i<=1:
	b=b+a[::-1]
	i=i+1
i=0
m=[]
while i<len(b):
	c=b[i].split()
	m.append(c)
	i+=1
print(m)