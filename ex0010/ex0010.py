from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
from PIL import ImageFilter
import random,string,PIL

def generateWords(y):
	return "".join((random.choice(string.ascii_letters)  for x in range(y)))

def generateTextColor():
	return(random.randint(125,255),random.randint(125,255),random.randint(125,255))

def generateBgColor():
	return(random.randint(0,125),random.randint(0,125),random.randint(0,125))


result = generateWords(4)
width = 200
height = 50
fontSize = 36
image = Image.new('RGB',(width,height),(84,84,84))
imageDraw = ImageDraw.Draw(image)
ft = ImageFont.truetype('arial.ttf',fontSize)

for x in range(width):
	for y in range(height):
		imageDraw.point((x,y),generateBgColor())

for i in range(len(result)):
	imageDraw.text((fontSize*i+36,10+random.randrange(-5,5)),result[i],font=ft,fill=generateTextColor())


blurImg = image.filter(ImageFilter.GaussianBlur(1))
blurImg.save("validtaion.png")
