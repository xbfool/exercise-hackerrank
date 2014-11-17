times = input()
for i in range(times):
	n = input()
	a = n * (n + 1) * (2 * n + 1) / 6

	b = (n + 1) * (n) / 2
	b = b * b
	print b - a