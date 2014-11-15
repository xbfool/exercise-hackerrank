n, m = map(int, raw_input().split())
edges = [-1] * (n + 1)
connected = [-1] * (n + 1)
for i in range(m):
	a,b = map(int, raw_input().split())
	edges[a] = b

ves = [1] * (n+1)

res = 0
for j in range(n, 1, -1):
	if ves[j] % 2 == 0:
		res += 1
	else:
		ves[edges[j]] += 1

print res 

