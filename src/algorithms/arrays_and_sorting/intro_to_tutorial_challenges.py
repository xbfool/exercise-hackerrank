v = input()
n = input()
numbers = [int(x) for x in raw_input().split()]
for i in range(n):
	if numbers[i] == v:
		print i
		break