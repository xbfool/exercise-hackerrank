n = input()
s = []
for i in range(n):
	s.append(list(raw_input()))

for j in range(1, n - 1):
	for i in range(1, n - 1):
		if (s[i - 1][j] == 'X' or s[i + 1][j] == 'X' or
			s[i][j - 1] == 'X' or s[i][j + 1] == 'X'):
			pass
		elif (int(s[i - 1][j]) < int(s[i][j]) and
			int(s[i + 1][j]) < int(s[i][j]) and
			int(s[i][j + 1]) < int(s[i][j]) and
			int(s[i][j - 1]) < int(s[i][j])):
			s[i][j] = 'X'
for i in s:
	print ''.join(i)

