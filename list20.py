a=[23,14,56,12,19,9,15,25,31,42,43]
i=0
num=0
sum=0
while i<len(a):
   sum=sum+i
   if a[i]%2==0:
       sum=sum+a[i]
   else:
       num=num+a[i]
i=i+1
rev=sum//len(a)
rev=num//len(a)
print("even num",rev) 
print("odd",rev)