a=[[1,2,3],[1,2,1],[5,3,5]]
i=0
max=0
b=[]
while i<len(a):
    j=0
    sum=0
    while j<len(a[i]):
        sum=sum+a[i][j]
        j=j+1
    b.append(sum)
    i=i+1
print(b)
for i in b:
    if i>max:
        max=i
print(max)


       