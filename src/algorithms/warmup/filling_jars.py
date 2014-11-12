s = [(int)(x) for x in (raw_input()).split(' ')]
n = s[0]
times = s[1]
total = 0
for i in range(times):
	k = [(int)(x) for x in (raw_input()).split(' ')]
	a = k[0]
	b = k[1]
	m = k[2]
	total += (b - a + 1) * m
print total / n