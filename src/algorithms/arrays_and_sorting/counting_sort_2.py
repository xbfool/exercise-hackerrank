count = input()
numbers = [(int)(x) for x in raw_input().strip().split()]
res = [0] * 100
for i in numbers:
	res[i] += 1

result = []
for j in range(len(res)):
	result.extend([j] * res[j])
print ' '.join([str(x) for x in result])
