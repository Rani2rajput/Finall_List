a=[3000,600000,324990909,90990900,30000,5600000,690909090,31010101,532010,510,4100]
i=0
sum=0
sum1=0
sum2=0
while i<len(a):
	if a[i]>=10000000:
		sum=sum+1
	elif a[i]>=100000:
		sum1=sum1+1
	else:
		sum2=sum2+1
	i=i+1
print("crorepati",sum)
print("lakhpati",sum1)
print("dilwale",sum2)