#coding=utf-8
import os,json,xlrd
from lxml import etree

workbook = xlrd.open_workbook('src.xls')
sheet = workbook.sheet_by_index(0)
directions = sheet.col_values(2,1,sheet.nrows)
durations = [int(x) for x in sheet.col_values(3,1,sheet.nrows)]

out_duration = []
in_duration = []

for x in range(0,len(directions)):
	if directions[x] == '主叫':
		out_duration.append(durations[x])
	else:
		in_duration.append(durations[x])

out_durations_sum = sum(x for x in out_duration)
in_durations_sum = sum(x for x in in_duration)
print("主叫总时长："+ str(out_durations_sum))
print("被叫总时长："+ str(in_durations_sum))

