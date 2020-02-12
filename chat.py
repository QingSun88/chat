
#读取档案
def read_file(filename):
	lines = []
	with open(filename, 'r', encoding='utf-8') as f:
		for line in f:
			lines.append(line.strip())
	return lines

#转换档案
def convert(lines):
	new = []    #暂存时候则考虑创建变数
	person = None #避免开头不是人名出现死循环，就先预设空无的值
	for line in lines:
		if line =='sunqing':
			person = 'sunqing'
			continue
		elif line =='brant':
			person = 'brant'
			continue
		if person:  #如果person有值则是真
		 	new.append(person + ': ' + line)
	return new

#输出档案
def write_file(filename, lines):
	with open(filename,'w') as f:
		for line in lines:
			f.write(line + '\n')


def main():
	lines = read_file('input.txt')
	lines = convert(lines)
	write_file('output.txt',lines)


main()

