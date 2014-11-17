from fractions import gcd

times = input()
for i in range(times):
	start = 1
	n = input()
	for i in range(n, 1, -1):
		x = gcd(start, i)
		start = start * i / x
	print start
