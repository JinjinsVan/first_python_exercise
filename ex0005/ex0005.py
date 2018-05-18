import os
import glob
from PIL import Image

ip5ImageWidth = 1136
ip5ImageHeight = 640

picList = glob.glob("*.jpg")
for pic in picList:
	file,ext = os.path.splitext(pic)
	im = Image.open(pic)
	w = im.size[0]
	h = im.size[1]
	if w*h > ip5ImageWidth*ip5ImageHeight:
		rs = ip5ImageWidth, h*(ip5ImageWidth/w)
		im.thumbnail(rs)
		im.save(file + "_thumbnail.jpg")