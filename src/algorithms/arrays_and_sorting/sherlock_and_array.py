times = input()
for i in range(times):
	n = input()
	ar1 = map(int, raw_input().split())
	total = sum(ar1)
	acc = 0
	for i in range(len(ar1)):
		if total - ar1[i] == 2 * acc:
			print "YES"
			break
		elif total - ar1[i] < 2 * acc:
			print "NO"
			break
		else:
			acc += ar1[i]