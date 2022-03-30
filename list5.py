a=[50,40,23,70,56,12,5]
i=0
count=0
while a[i:]:
    num=a[i]
    if num>=20 and num<=40:
        count=count+1
    i=i+1
print(count)
        