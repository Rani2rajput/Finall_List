a=[2,5,8,9,4,6,3]
i=0
c=0
c1=0
while i<len(a):
	if a[i]%2==0:
		c=c+1
	else:
		c1=c1+1
	i=i+1
print("even",c)
print("odd",c1)