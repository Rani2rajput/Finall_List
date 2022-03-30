num=input("enter any char of list::")
a=["A","B","C"]
b=[[1,2],[3,4],[5,6]]
i=0
while i<len(a):
	if num==a[i]:
		print(b[i])
	i+=1