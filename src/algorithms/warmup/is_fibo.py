times = input()
fibolist = [1,1]
fiboset = set(fibolist)
for i in range(times):
	s = input()
	while fibolist[-1] < s:
		x = fibolist[-1] + fibolist[-2]
		fibolist.append(x)
		fiboset.add(x)
	
	if s in fiboset:
		print "IsFibo"
	elif fibolist[-1] > s:
		print "IsNotFibo"
