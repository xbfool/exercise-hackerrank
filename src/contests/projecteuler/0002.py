times = input()
for i in range(times):
	n = input()
	total = 0
	a, b = 1, 1
	while b < n:
		a, b =  b, a + b
		if b % 2 == 0 and b < n:
			total += b
	print total