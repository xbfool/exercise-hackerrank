from collections import deque
n, k, q = map(int, raw_input().split())
ar = deque(map(int, raw_input().split()))
ar.rotate(k)
for i in range(q):
	print ar[input()]

