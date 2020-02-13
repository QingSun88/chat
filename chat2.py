
#读取档案
def read_file(filename):
	lines = []
	with open(filename, 'r', encoding='utf-8-sig') as f:
		for line in f:
			lines.append(line.strip())
	return lines


#转换档案
def convert(lines):
	new = []    #暂存时候则考虑创建变数
	person = None #避免开头不是人名出现死循环，就先预设空无的值
	allen_word_count = 0
	viki_word_count = 0
	for line in lines:
		s = line.split(' ')
		time = s[0]
		name = s[1]
		if name == 'Allen':
			for m in s[2:]:
				allen_word_count += len(m)
			
		elif name == 'Viki':
			for m in s[2:]:
				viki_word_count += len(m)
			
	print('allen said', allen_word_count)
	print('viki said', viki_word_count)

		# print(s)
	return new


#输出档案
def write_file(filename, lines):
	with open(filename,'w') as f:
		for line in lines:
			f.write(line + '\n')


def main():
	lines = read_file('Viki.txt')
	lines = convert(lines)
	# write_file('output.txt',lines)


main()

