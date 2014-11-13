number = input()
number_array = [(int)(x) for x in raw_input().split()]
total = 0
for i in range(1, number):
	for j in range(i):
		ii = number_array[i]
		jj = number_array[j]
		if  ii < jj:
			total += i - j
			number_array = number_array[:j] +  [ii] + [jj] + number_array[j+1:i] +  number_array[i+1:]
			break
print total


