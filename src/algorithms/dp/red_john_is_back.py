times = input()
ar = [0,1,1,1,2]
def primes(n):
	if n < 2:
		return []
	""" Returns  a list of primes <= n """
	n = n + 1
	sieve = [True] * n
	for i in xrange(3,int(n**0.5)+1,2):
		if sieve[i]:
			sieve[i*i::2*i]=[False]*((n-i*i-1)/(2*i)+1)
	return [2] + [i for i in xrange(3,n,2) if sieve[i]]

for j in range(len(ar), 41):
		ar.append(ar[j-1] + ar[j-4])

for i in range(times):
	a = input()
	t = ar[a]
	print len(primes(t))

