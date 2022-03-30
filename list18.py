x=[1,'liza',[4,5],'himani',9,7]
i=0
while i<len(x):
    j=0
    sum=0
    while j<len(x):
        if i==j:                
            pass
        else:
            sum=sum+i
        j+=1
    i+=1           
print(sum)