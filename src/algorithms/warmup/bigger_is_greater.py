def get_bigger(s):
	#get the first little
	index = -1
	for i in range(len(s) - 1, 0, -1):
		if(ord(s[i]) > ord(s[i-1])):
			index = i - 1
			break
	if index == -1:
		print 'no answer'
		return
	#change first
	min_max = 999
	index_2 = -1
	for i in range(index + 1, len(s)):
		if ord(s[i]) > ord(s[index]) and ord(s[i]) < min_max:
			index_2 = i
			min_max = ord(s[i])

	s = list(s)
	s[index], s[index_2] = s[index_2], s[index]
	s_temp = s[index + 1:]
	if index + 1 < len(s) - 1:
		s_temp.sort()
		#s_temp.reverse()
		res = s[0:index + 1] +  s_temp
	else:
		res = s
	print ''.join(res)

times = input()
for i in range(times):
	s = raw_input()
	get_bigger(s)