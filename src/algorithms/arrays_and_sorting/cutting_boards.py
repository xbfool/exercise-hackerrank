times = input()
for i in range(times):
	m, n = map(int, raw_input().split())
	ar1 = sorted(map(int, raw_input().split()))
	ar1.reverse()
	ar2 = sorted(map(int, raw_input().split()))
	ar2.reverse()
	index1 = 0
	index2 = 0
	total = 0
	while index1 < len(ar1) and index2 < len(ar2):
		if ar1[index1] > ar2[index2]:
			total += ar1[index1] * (index2 + 1) % 1000000007
			index1 += 1
		else:
			total += ar2[index2] * (index1 + 1) % 1000000007
			index2 += 1

	while index1 < len(ar1):
		
		total += ar1[index1] * (index2 + 1) % 1000000007
		index1 += 1

	while index2 < len(ar2):
		
		total += ar2[index2] * (index1 + 1) % 1000000007
		index2 += 1

	print total % 1000000007