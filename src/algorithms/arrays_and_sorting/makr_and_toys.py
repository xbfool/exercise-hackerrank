s = [int(x) for x in raw_input().split()]
n = s[0]
m = s[1]
ar = [int(x) for x in raw_input().split()]
ar.sort()
index = 0
for i in ar:
	m -= i
	if m < 0:
		break
	else:
		index += 1
print index
