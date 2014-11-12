def get_num(a, b):
	res = 0
	for i in range(len(a)):
		if a[i] == '1' or b[i] == '1':
			res += 1
	return res

s = [(int)(x) for x in (raw_input()).split(' ')]
n = s[0]
m = s[1]
arr = []
for i in range(n):
	arr.append(raw_input())

max_num = 0
max_index = 0
for j in range(n):
	for k in range(j + 1, n):
		num = get_num(arr[j], arr[k])
		if max_num < num:
			max_num = num
			max_index = 1
		elif max_num == num:
			max_index += 1
print max_num
print max_index