#python2.x
times = (int)(raw_input())
s = raw_input()
ssplit = s.split(' ')
inta = [(int)(x) for x in ssplit]
inta = inta[0:times]
res = []
while len(inta) > 0:
	res.append(len(inta))
	inta = [ x - min(inta) for x in inta if x > min(inta)]

for i in res:
	print i