from collections import Counter
times = (int)(raw_input())
for i in range(times):
	n = (int)(raw_input())
	a = (int)(raw_input())
	b = (int)(raw_input())
	res = []
	for j in range(n):
		res.append(j * b + (n - j - 1) * a)
	c = Counter(res)
	result = c.keys()
	result.sort()
	print ' '.join([str(x) for x in result])