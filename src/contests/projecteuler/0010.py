def get_primes(n):
	numbers = set(range(n, 1, -1))
	primes = []
	while numbers:
		p = numbers.pop()
		primes.append(p)
		numbers.difference_update(set(range(p*2, n+1, p)))
	return primes

from bisect import *


times = input()
params = []
m = 0
for i in range(times):
	a = input()
	m = max(m, a)
	params.append(a)

ar = get_primes(m)

ar.sort()
ar2 = []
accu = 0
for i in ar:
	accu += i
	ar2.append(accu)

for item in params:
	n = item 
	index = bisect(ar, n)

	if index <= 0:
		print 0
	else:
		print ar2[index - 1]
