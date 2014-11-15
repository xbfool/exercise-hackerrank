from collections import Counter
times = input()
for i in range(times):
	n = input()
	ar = map(int, raw_input().split())
	c = Counter(ar)
	l = len(ar)
	total = 0
	for i in c.values():
		total += i * (i - 1)
	print total