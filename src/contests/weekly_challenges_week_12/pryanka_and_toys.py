from collections import *
count = input()
ar = map(int, raw_input().split())
ar.sort()
dar = deque(ar)
start = 1

temp = 0
temp = dar[0]
while len(dar) > 0:
	t = dar.popleft()
	if t > temp + 4:
		start += 1
		temp = t
print start
