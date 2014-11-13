params = [(int)(x) for x in raw_input().split(' ')]
n = params[0]
t = params[1]
high_array = [(int)(x) for x in raw_input().split(' ')]
#test_case_array = []
for ii in range(t):
	case = [(int)(x) for x in raw_input().split(' ')]
	m = 10
	i = case[0]
	j = case[1]
	for kk in range(i, j + 1):
		m = min(high_array[kk], m)
	print m 