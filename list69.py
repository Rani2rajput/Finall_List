a=[[1,4],[3,2,6],[5,8],[1]]
i =0
max=0
min=0
while i<len(a):
  if len(a[i])>min:
    min=len(a[i])
    max=a[i]
  i=i+1
print(max)