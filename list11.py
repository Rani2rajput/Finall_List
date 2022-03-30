a=[1,2,3,4,5,6]
b=[2,3,1,0,6,7]
i=0
s=[]
while i<len(a):
    if a[i] not in b:
        s.append(a[i])
    i=i+1
print(s)
        