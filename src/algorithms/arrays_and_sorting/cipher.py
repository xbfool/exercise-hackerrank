n,k = map(int, raw_input().split())
out = map(int, list(raw_input()))
ori = [0] * n
offset = 0
for i in range(n):
	if i >= 1:
		offset ^= ori[i - 1]
	if i >= k:
		offset ^= ori[i - k]
	ori[i] = offset ^out[i]
print ''.join(map(str, ori))