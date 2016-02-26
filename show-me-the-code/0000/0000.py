from PIL import Image, ImageDraw, ImageFont
import os

def addNum(filePath, num):
	img = Image.open(filePath)
	w, h = img.size
	fontSize = h // 4
	draw = ImageDraw.Draw(img)

	ttFont = ImageFont.truetype("/Library/Fonts/arial.ttf", fontSize)
	draw.text((w - fontSize, 0), str(num), (255, 0, 0), font = ttFont)
	del draw
	# 
	if(os.path.exists("result.jpg")):
		os.remove("result.jpg")

	img.save("./result.jpg")
	img.show()

if __name__ == '__main__':
	pathStr = 'image.jpg'
	num = int(input("Please input the number you wanted to add: "))
	if(os.path.exists(pathStr)):
		addNum(pathStr, num)
	else:
		print("import image failed!")