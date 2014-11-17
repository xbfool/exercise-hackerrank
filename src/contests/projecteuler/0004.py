from copy import copy
def checknumber(n):
	a = list(str(n))
	b = list(str(n))
	b.reverse()
	return cmp(a, b)

def genall():
	l = set()
	for i in range (100, 999):
		for j in range(100, 999):
			if checknumber(i * j) == 0:
				l.add(i * j)
	l = list(l)
	l.sort()
	return l


times = input()
l = genall()

for i in range(times):
	a = input()
	for j in range(len(l)):
		if l[j] >= a:
			print l[j - 1]
			break

