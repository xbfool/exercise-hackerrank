from math import ceil, floor, sqrt
times = (int)(raw_input())
for i in range(times):
	s = raw_input()
	a = (int)((s.split(' '))[0])
	b = (int)((s.split(' '))[1])
	a_1 = ceil(sqrt(a))
	b_1 = floor(sqrt(b))
	print max((int)(b_1 - a_1 + 1), 0)
