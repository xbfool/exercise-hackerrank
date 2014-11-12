times = (int)(raw_input())
for i in range(times):
	s = raw_input()
	s_int = (int)(s)
	res = 0
	for j in s:
		if (int)(j) == 0:
			pass
		elif s_int % (int)(j) == 0:
			res += 1
	print res