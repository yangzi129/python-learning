# -*- coding: utf-8 -*-

import glob, os
from PIL import Image

def process(SrcFilePath, DesFilePath):
	f = Image.open(SrcFilePath)
	newFile = f.resize((1136, 640))
	# 该文件已经存在 则删除
	if(os.path.exists(DesFilePath)):
		os.remove(DesFilePath)
	newFile.save(DesFilePath)

if __name__ == '__main__':
	Dir = "test/" # 待处理图片所在文件夹
	resDir = "result/" # 处理完图片存放文件夹
	f_list = glob.glob(Dir + "*.jpg") # 查找匹配文件路径
	if(len(f_list) == 0):
		print(".jpg Not Found!")
		exit()

	for f in f_list:
		process(f, resDir + os.path.basename(f))

	print("finished!")