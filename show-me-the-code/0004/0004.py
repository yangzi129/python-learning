# -*- coding: utf-8 -*-

# 正则匹配
import os, re

def calc(f):
	words = re.findall(r'[a-zA-Z]+(\'[a-zA-Z]+|\b)', f) 
	# print(words)
	return len(words)

if __name__ == '__main__':
	if(os.path.exists("test.txt") == False):
		print("Not found test.txt")
		exit()

	with open("test.txt", "r") as f:
		res = calc(f.read())

	print("There are %d words\n" % res)