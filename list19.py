num=int(input("enter any num"))
x=num
sum=0
i=0
while num>0:
    sum=sum+x
    k=(num%10)+(num%10)+(num%10)
    num=k//10

if x==sum:
    print("armstrong")
else:
    print("not armstrong")

