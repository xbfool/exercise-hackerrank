count = input()
res = [0] * 100
result = [0] * 100
for i in range(count):
	n = int(raw_input().strip().split()[0])
	res[n] += 1
for j in range(100):
	if j == 0:
		result[j] = res[j]
	else:
		result[j] = res[j] + result[j - 1]
print ' '.join(str(x) for x in result)