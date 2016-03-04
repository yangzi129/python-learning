# -*- coding: utf-8 -*-

import glob, os, re

def wordsFreq(filePath):
	with open(filePath) as f:
		s = f.readline()
		st = {}
		# 逐行读取文件
		while(s):
			# 以空格分割 标点符号会有问题
			words = s.strip().split()
			for w in words:
				if w in st:
					st[w] += 1
				else :
					st[w] = 1
			s = f.readline()

		res = []
		maxV = 0
		for key in st:
			vis = st[key]
			if vis > maxV :
				maxV = vis
				res = [key]
			elif vis == maxV:
				res += [key]
		return res, maxV

if __name__ == '__main__':
	Dir = "test/"
	files = glob.glob(Dir + "*.txt")
	for f in files:
		resStr, times = wordsFreq(f)
		print("The most occurance of these words in file \"%s\" are %d times:" % (f, times))
		for w in resStr:
			print("%s" % w, end = " ")
		print()
