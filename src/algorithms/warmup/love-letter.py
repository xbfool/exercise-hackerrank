#python2.x
times = (int)(raw_input())
res_array = []
for i in range(times):
	s = raw_input()
	l = len(s)
	res = 0
	for j in range(l / 2):
		res += abs(ord(s[j]) - ord(s[l-j-1]))
	res_array.append(res)

for r in res_array:
	print r