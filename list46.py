a=["1","2","3","4"]
i=0
sum=0
s=[]
while i<len(a):
	sum=int(a[i])+1
	s.append(str(sum))
	i=i+1
print(s)