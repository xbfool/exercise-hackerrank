
times = input()
for i in range(times):
	m, n = map(int, raw_input().split())
	s = map(int, raw_input())
	max_n = 0
	for i in range(m - n):
		temp = 1
		for j in range(i, i + n):
			temp *= s[j]
		max_n = max(max_n, temp)
	print max_n