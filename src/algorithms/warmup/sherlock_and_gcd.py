from collections import Counter
from fractions import *
times = (int)(raw_input())
for i in range(times):
	numbers = (int)(raw_input())
	s = raw_input()
	s = s.split(' ')
	s = s[0:numbers + 1]
	s = [(int)(x) for x in s]
	g = s[0]
	for j in s:
		g = gcd(g, j)
	if g > 1:
		print "NO"
	else:
		print "YES"