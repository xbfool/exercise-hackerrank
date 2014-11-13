
times = input()
for i in range(times):
	count = input()
	numbers =[int(x) for x in raw_input().split()]
	if count % 2 == 0:
		print 0
	else:
		start = 0
		for i in range(0, count, 2):
			start ^= numbers[i]
		print start

