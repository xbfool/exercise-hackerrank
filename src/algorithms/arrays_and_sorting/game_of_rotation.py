times = input()
ar = map(int, raw_input().split())
total = sum(ar)
max_pem = 0
for i in range(len(ar)):
	max_pem += (i + 1) * ar[i]

tmp_pem = max_pem

for item in ar:
	tmp_pem = tmp_pem - total + len(ar) * item
	max_pem = max(tmp_pem, max_pem)

print max_pem
