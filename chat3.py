
lines = []
with open('3.txt', 'r',encoding= 'utf-8-sig') as f:
	for line in f:
		lines.append(line.strip())

for line in lines:
	s = line.split(' ')
	time = s[0][:5]   #清单分割法将清单中固定位置的东西取出
	name = s[0][5:]   #字串也可当做清单处理
	print(time)
	print(name)