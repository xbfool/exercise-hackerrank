times = input()
for i in range(times):
	s = map(int, raw_input().split())
	n = s[0]
	k = s[1]
	ar1 = map(int, raw_input().split())
	ar2 = map(int, raw_input().split())
	ar1.sort()
	ar2.sort()
	ar2.reverse()
	r = True
	for i in range(len(ar1)):
		if ar1[i] + ar2[i] < k:
			r = False
			break
	if r == True:
		print "YES"
	else:
		print "NO"