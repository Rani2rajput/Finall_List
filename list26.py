a="ranirajput"
i=0
while i<len(a):
	count=0
	j=0
	while j<len(a):
		if a[i]==a[j]:
			count=count+1
		j=j+1
		k=a[i]
	print(k,count)
	i=i+1