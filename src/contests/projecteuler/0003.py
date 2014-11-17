def get_primes(n):
	numbers = set(range(n, 1, -1))
	primes = []
	while numbers:
		p = numbers.pop()
		primes.append(p)
		numbers.difference_update(set(range(p*2, n+1, p)))
	return primes
import math
def get_first_factor(n, l):
	for i in l:
		if n % i == 0:
			return i
	return n

times = input()
for i in range(times):
	n = input()
	l = get_primes(int(math.floor(math.sqrt(n))))
	max_factor = 1

	while n > 1:
		f = get_first_factor(n, l)
		max_factor = max(f, max_factor)
		n = n / f

	print max_factor