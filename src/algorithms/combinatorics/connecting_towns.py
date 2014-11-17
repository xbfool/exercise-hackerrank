times = input()
for i in range(times):
	n = input()
	ar = map(int, raw_input().split())
	r = reduce(lambda x, y:  x * y % 1234567, ar)
	print r