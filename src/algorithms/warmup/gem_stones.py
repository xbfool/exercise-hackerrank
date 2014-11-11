#python2.x
times = (int)(raw_input())
s = []
for i in range(times):
	ss = set(raw_input())
	s.append(ss)

res = s[0]
for j in s:
	res = set.intersection(res, j)

print len(res)