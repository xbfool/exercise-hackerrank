times = input()

def getx(n, a):
	n = n - 1
	x = n / a
	res = x * (x + 1) * a / 2
	return res

for i in range(times):
	n = input()
	print getx(n, 3) + getx(n, 5) - getx(n, 15)