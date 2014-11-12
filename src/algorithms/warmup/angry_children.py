n = input()
k = input()
candies = [input() for _ in range(0,n)]
candies.sort()

min_diff = candies[n - 1]
for i in range(n - k + 1):
	min_diff = min(candies[i + k - 1] - candies[i], min_diff)

print min_diff

