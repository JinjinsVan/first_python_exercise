#coding=utf-8
import os,json,xlrd
from lxml import etree

workbook = xlrd.open_workbook('numbers.xlsx')
sheet = workbook.sheet_by_index(0)

data = []
for row in range(sheet.nrows):
	r_index_list = []
	for col in range(sheet.ncols):
		r_index_list.append(int(sheet.cell_value(row,col)))
	data.append(r_index_list)

root = etree.Element('root')
numbers = etree.SubElement(root,sheet.name)
numbers.append(etree.Comment(u'''数字信息'''))
numbers.text = json.dumps(data,ensure_ascii=False)
tree = etree.ElementTree(root)
tree.write('numbers.xml',pretty_print=True,xml_declaration=True, encoding='utf-8')


