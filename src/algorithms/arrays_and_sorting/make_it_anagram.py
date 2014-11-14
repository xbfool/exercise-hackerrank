from collections import Counter
a = Counter(raw_input())
b = Counter(raw_input())
a.subtract(b)
for i in a.keys():
	if(a[i] < 0):
		a[i] = -a[i]
print sum(a.values())
 