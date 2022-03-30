number=[50,40,23,70,56,12,5,10,7]
i=0
max=0
while i<len(number):
    if number[i]>max:
        max=number[i]
    i=i+1
print(max)
j=0
smax=0
while j<len(number):
    if number[j]<max:
        if number[j]>smax:
            smax=number[j]

    j=j+1
print(smax)