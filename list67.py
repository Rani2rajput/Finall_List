l1=["a","b","c"]
l2=[1,2,3]
dic={}
list=[]
for i in l1:
    for j in l2:
        if i in j:
            list.append(l1)
            list.append(l2)
print(list)

#         if i in j:
#             dic.update(i)
#             dic.update(j)
# print(dic)
            
        