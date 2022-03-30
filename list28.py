num=[11,23,45,99]
m=[]
i=0
while i<len(num):
	s=""
	j=0
	d=str(num[i])
	while j<len(d):
		if d[j]=="1":
			s=s+"one,"
		elif d[j]=="2":
			s=s+"two,"
		elif d[j]=="3":
			s=s+"three,"
		elif d[j]=="4":
			s=s+"four,"
		elif d[j]=="5":
			s=s+"five,"
		elif d[j]=="6":
			s=s+"six,"
		elif d[j]=="7, ":
			s=s+"seven,"
		elif d[j]=="8":
			s=s+"eight,"
		elif d[j]=="9":
			s=s+"nine,"
		elif d[j]=="0":
			s=s+"zero,"
		j=j+1
	i=i+1
	m.append(s)
print(m)
