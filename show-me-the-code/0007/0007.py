import glob

# 判断字符串类型 统计对应数字
def addIt(line, l):
	# print(l)
	line = line.lstrip()
	l[0] += 1
	if line == "":
		l[1] += 1
	else:
		if len(line) > 0 and line[0] == '/':
			l[2] += 1

# 统计当前文件
def calc(filePath):
	res = [0, 0, 0]
	with open(filePath, "r") as f:
		L = f.readline()
		addIt(L, res)
		while(L):
			addIt(L, res)
			L = f.readline()
	return res

if __name__ == '__main__':
	# 扫描目标文件夹 cpp 文件
	Dir = "test/"
	files = glob.glob(Dir + "*.cpp")
	totolLines, emptyLines, noteLines = 0, 0, 0 
	for f in files:
		t = calc(f)
		totolLines += t[0]
		emptyLines += t[1]
		noteLines += t[2]
	
	print("results:")
	print("totolLines : %d" % totolLines)
	print("emptyLines : %d" % emptyLines)
	print("noteLines: %d" % noteLines)