number=[50,40,23,70,56,12,5,10,7]
i=0
min=number[i]
while i<len(number):
    if number[i]<min:
        min=number[i]
    i=i+1
print(min)
j=0
smin=number[j]
while j<len(number):
    if number[j]>min:
        if number[j]<smin:
            smin=number[j]
    j=j+1
print(smin)
        