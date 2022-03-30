list=[1,2,3,[4,5,6],7,8]
i=0

list1=[]
while i <len(list):
    j=0
    sum=0
    while j<list[i]:
        sum=sum+list[i][j]
        print(j)
        # list1.append(i)
        # list1.append(j) 
        j=j+1
    i=i+1
# print(list1)       


# for i in list:
#     # print(i)
#     for j in list[2] :
#         print(j)
# while i <len(list):
#     j=0
#     while j<len(list[2]):
#         print(j)
# for i in list[1]:
#     print(i)
#     for j in list[2]:
#         print(j)
    # j=0
    # while j<len(list[i]):
    #     print(j)
    #     j=j+1
    # i=i+1
