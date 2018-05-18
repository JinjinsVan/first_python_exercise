#coding=utf-8
import os,json
from lxml import etree
import xlrd 

workbook = xlrd.open_workbook("students.xlsx")
sheet = workbook.sheets()[0]
dic = dict()
for rowindex in range(sheet.nrows):
	dic[str(rowindex)]=[]
	for colindex in range(1,sheet.ncols):
		dic[str(rowindex)].append(sheet.cell_value(rowindex,colindex))

rootElement = etree.Element("root")
studentsElement = etree.SubElement(rootElement,"students")
comm = etree.Comment(u'''学生信息表
					    "id" : [名字, 数学, 语文, 英文] ''')

studentsElement.append(comm)
stuEleValue = json.dumps(dic,ensure_ascii=False)
studentsElement.text = stuEleValue
tree = etree.ElementTree(rootElement)
tree.write("students.xml", pretty_print=True,xml_declaration=True, encoding='utf-8')

