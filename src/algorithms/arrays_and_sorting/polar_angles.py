times = input()
angles = []
for i in range(times):
	angles.append(map(int, raw_input().split()))

from math import atan2, hypot,pi

def new_atan2(y, x):
	tmp = atan2(y, x)
	if tmp < 0:
		tmp += 2 * pi
	return tmp
def cmp_1(x, y):
	if atan2(x[1], x[0]) == atan2(y[1], y[0]):
		return cmp(hypot(x[1], x[0]),hypot(y[1], y[0]))
	else:

		return cmp(new_atan2(x[1], x[0]),new_atan2(y[1], y[0]))
new = sorted(angles, cmp_1)
for i in new:
	print '%d %d' % (i[0], i[1])