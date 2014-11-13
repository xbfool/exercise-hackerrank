def xpower(s, n):
	if n % 2 == 0:
		temp = xpower(s, n/2)
		return (temp * temp) % (1000000000 + 7)
	elif n == 1:
		return s
	else
		temp = xpower(s, n/2)
		return (temp * temp * s) % (1000000000 + 7)

mn = [(int)(x) for x in raw_input().split(' ')]
n = mn[0]
m = mn[1]

alist = [(int)(x) for x in raw_input().split(' ')][0:n]
blist = [(int)(x) for x in raw_input().split(' ')][0:m]
clist = [(int)(x) for x in raw_input().split(' ')][0:m]
clist_result = [-1] * m

for i in range(0, m):
	for j in range(0, n + 1, blist[i]):
		if j - 1 < 0:
			pass
		else:
			alist[j - 1] = (alist[j - 1] * clist[i]) % (1000000000 + 7)

alist = [str(x) for x in alist]
print ' '.join(alist)