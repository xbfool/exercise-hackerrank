times = (int)(raw_input())
for i in range(times):
	n = (int)(raw_input())
	a = n % 3
	if(a == 0):
		print '5' * n
	elif(a == 1):
		if n >= 10:
			print '5' * (n - 10)+'3' * 10
		else:
			print -1
	elif(a == 2):
		if n >= 5:
			print '5' * (n - 5)+'3' * 5
		else:
			print -1
