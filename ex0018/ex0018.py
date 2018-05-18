#coding=utf-8
import os,json
from lxml import etree
import xlrd 

workbook = xlrd.open_workbook('cities.xlsx')
sheet = workbook.sheet_by_index(0)
dic = dict()
for row in range(sheet.nrows):
	for col in range(sheet.ncols):
		dic[str(row+1)] = sheet.cell_value(row,col)

root = etree.Element('root')
cities = etree.SubElement(root,sheet.name)
cities.append(etree.Comment(u'''城市信息'''))
cities.text = json.dumps(dic,ensure_ascii=False)
tree = etree.ElementTree(root)
tree.write("cities.xml",pretty_print=True,xml_declaration=True, encoding='utf-8')
