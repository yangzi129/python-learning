import random


def generator(len = 8):
	s = ""
	for i in range(len):
		num = random.randint(0, 61)
		if num <= 9:
			s += str(num)
		elif num <= 35:
			s += chr(num - 10 + ord('a'))
		else:
			s += chr(num - 36 + ord('A'))
	# print("\n%s" % s)
	return s

if __name__ == '__main__':
	# 随机生成 num 个字符串
	num = 200
	res = set()
	while num > 0:
		num = num - 1
		tmpStr = generator()
		while tmpStr in res:
			tmpStr = generator()
		res.add(tmpStr)
	# print(len(res))
	f = open("result.txt", "w")
	for s in res:
		f.write(s + "\n")
	f.close()