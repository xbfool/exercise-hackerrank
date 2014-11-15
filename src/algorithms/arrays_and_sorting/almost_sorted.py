from copy import copy
count = input()
ori = map(int, raw_input().split())
sorted_ori = copy(ori)
sorted_ori.sort()
for i in range(len(ori)):
	if sorted_ori[i] == ori[i]:
		sorted_ori[i] = -1

index = 0
a_index = -1
b_index = -1

for i in range(len(ori)):
	if sorted_ori[i] != -1:
		if index == 0:
			a_index = i
		elif index == 1:
			b_index = i
		index += 1


if index == 0:
	print "yes"
elif index == 2:
	print "yes"
	print 'swap %d %d' %(a_index + 1, b_index + 1)
else:
	status = 0
	start = -1
	end = -1
	for i in range(len(ori)):
		if status == 3:
			#3代表坏了
			break
		elif sorted_ori[i] != -1:
			#可能是reverse状态
			if status == 0:
				#刚进来
				status = 1
				start = i
			elif status == 1:
				if ori[i] < ori[i - 1]:
					#正常
					end = i
				else:
					#坏了
					status = 3
			elif status == 2:
				status = 3
		elif sorted_ori[i] == -1:
			if status == 0:
				pass
			elif status == 1:
				#有可能还在继续
				if ori[i] < ori[i - 1]:
					end = i
				else:
					status = 2
					end = i - 1
			elif status == 2:
				pass
	if status == 2 or status == 1:
		print "yes"
		print 'reverse %d %d' % (start + 1, end + 1)
	else:
		print 'no'
