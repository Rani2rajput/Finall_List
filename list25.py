n=[23,14,56,12,19,9,15,26,31,42]
i=0
sum=0
while i<len(n):
	sum=sum+n[i]
	if n[i]==19:
		break
	print(sum)
	i+=1