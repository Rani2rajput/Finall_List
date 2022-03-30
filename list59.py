m="the quick brown for jumped over the lazy dog the dog slept over the verandah"
a=m.split()
i=0
while i<len(a):
	if a[i]=="dog":
		a.remove("dog")
	i=i+1
me2=" ".join(a)
print(me2)