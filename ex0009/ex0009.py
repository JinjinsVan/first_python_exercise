from urllib.parse import urlparse
from html.parser import HTMLParser
from html.entities import name2codepoint
from xml.etree.ElementTree import ElementTree
import urllib.request
import re


class MyHTMLParser(HTMLParser):
	def handle_starttag(self,tag,attrs):
		if tag == 'a' and (attr[1].startswith('http') for attr in attrs):
			for attr in attrs:
				if attr[1].startswith('http'):
					self.links.append(attr[1])
		else:
			return

url = "http://linux.vbird.org/vbird/"
parser = MyHTMLParser()
parser.links = []
response = str(urllib.request.urlopen(url).read(),'utf-8')
parser.feed(response)
for l in parser.links:
        print(l)


# print(response)