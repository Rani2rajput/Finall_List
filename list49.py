a=[['A','B'],['A','C'],['A','B','C']]
i=0
count=0
while i<len(a):
	j=0
	while j<len(a[i]):
		if a[i][j]=='A':
			count=count+1
		j=j+1
	i=i+1
print(count)