list=[0,1,2,3,4,2,5,2]
i=0
count=0
while i<len(list):
	if list[i]==2:
		count=count+1
	i=i+1
print(count)