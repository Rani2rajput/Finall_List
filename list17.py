n=[10,11,12,13,14,17,18,19]
i=0
list1=[]
while i<len(n):
    list2=[]
    j=i
    while j<len(n):
        if n[i]+n[j]==30:
            list2.append(n[i])
            list2.append(n[j])
            list1.append(list2) 
        j=j+1
    i=i+1
print(list1)                                                                                                                          
    
    


