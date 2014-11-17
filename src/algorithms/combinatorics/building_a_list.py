from itertools import *

times = input()
for i in range(times):
	l = input()
	ar = raw_input()
	r = []
	for i in range(1, l + 1):	
		slist = combinations(ar, i)
		r.extend(slist)
		r.sort()
	for item in r:
		print item