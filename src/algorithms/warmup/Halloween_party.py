#python2.x
times = (int)(raw_input())
res_array = []
for i in range(times):
	s = int(raw_input())
	a = s / 2
	b = s - a
	res = a * b
	res_array.append(res)

for r in res_array:
	print r