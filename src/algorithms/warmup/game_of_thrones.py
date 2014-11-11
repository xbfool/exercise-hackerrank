from collections import Counter
string = raw_input()

s = 0
c = Counter(string)
for i in c.values():
	if i % 2 == 1:
		s += 1
if s <= 1:
	found = True
else:
	found = False
# Write the code to find the required palindrome and then assign the variable 'found' a value of True or False

if not found:
    print("NO")
else:
    print("YES")

