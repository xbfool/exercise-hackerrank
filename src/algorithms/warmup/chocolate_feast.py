T = int(raw_input())
for i in range (0,T):
	A,B,C1 = [int(x) for x in raw_input().split(' ')]

	if C1 > 0:
		base = A / B

		no_warppers = base
		while no_warppers > 0 and no_warppers >= C1:
			base += no_warppers / C1
			no_warppers = no_warppers % C1 + no_warppers / C1
		# write code to compute answer
		print base

	else:
		answer = A / B
		print answer
