import cProfile
import re
import math

def bbb():
	times = input()
	l = [x * x for x in range(3000)]
	kmax = [-1] * 3001

	for a in range(1, 1001):
		for b in range(a, 1501):
			c = int(math.sqrt(l[a] + l[b]))
			if l[a] + l[b] == l[c] and a + b + c <= 3000:
				kmax[a+b+c] = max(kmax[a+b+c], a * b * c)
	for i in range(times):
		n = input()
		print kmax[n]
		


def aaa():
	times = 3000
	l = [x * x for x in range(3000)]
	kmax = [-2] * 3001

	for i in range(times):
		n = i
		if kmax[n] > -2:
			found = True
		else:
			found = False
		for a in range(n/3, 0, -1):
			if found:
				break
			for b in range(a, n / 2 + 1):
				if n - a - b <= b:
					break
				a1 = l[a] + l[b]
				a2 = l[n - a - b]

				if a1 == a2:
			#		print a, b, n - a - b
					kmax[n] =  a * b * (n - a - b)
					found = True
					break
				elif a1 > a2:
					break
		if not found:
			kmax[n] = -1
		print kmax[n]

bbb()
