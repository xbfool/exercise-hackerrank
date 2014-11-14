#!/bin/python
def partition(ar):    
	left = []
	right = [ar[0]]
	p = ar[0]
	for i in ar[1:]:
		if i < p:
			left.append(i)
		else:
			right.append(i)
	return left + right

m = input()
ar = [int(i) for i in raw_input().strip().split()]
result = partition(ar)
print ' '.join([str(x) for x in result])

