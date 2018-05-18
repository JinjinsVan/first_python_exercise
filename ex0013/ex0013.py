from urllib.parse import urlparse
from html.parser import HTMLParser
import urllib.request,re,time,os
from PIL import ImageFile


class MyHTMLParser(HTMLParser):
	def handle_starttag(self,tag,attrs):
		if tag == 'img':
			for attr in attrs:
				if attr[0] == 'src' and re.match(r"^http.*(jpg|png|jpeg|gif)$",attr[1]):
					self.imgs.append(attr[1])

# 过滤掉尺寸过小的图片，比如头像、表情之类的
def filterSmallImage(picUrls):
	resultList = []
	for url in picUrls:
		file = urllib.request.urlopen(url)
		size = file.headers.get("content-length")
		if size: size = int(size)
		parser = ImageFile.Parser()
		parser.feed(file.read())
		if parser.image:
			size = parser.image.size
			if size[0]>200 and size[1]>200:
				resultList.append(url)
		file.close		
	return resultList


					
parser = MyHTMLParser()
parser.imgs = []
url = 'http://tieba.baidu.com/p/2166231880'
htmlContent = str(urllib.request.urlopen(url).read(),'utf-8')
parser.feed(htmlContent)


cwd = os.getcwd()
savePath = os.path.join(cwd,"ex0013Images")
if not os.path.exists(savePath):
	os.mkdir(savePath)

trueImages = filterSmallImage(parser.imgs)

for imgLink in trueImages:
	imgName = imgLink.split("/")[-1]
	urllib.request.urlretrieve(imgLink,os.path.join(savePath,imgName))