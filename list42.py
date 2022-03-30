a=[5,2,3,7,9,6,4]
b=[2,7,1,0,8,5,4]
i=0
m=[]
while i<len(a):
	if a[i]not in b:
		m.append(a[i])
	i=i+1
print(m)