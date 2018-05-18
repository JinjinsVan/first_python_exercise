import io
import re

resultDic = dict()
# resultDic["delmar"]=1
# print("delmar" in resultDic)
f = open("ex0004test.txt",'r')
for line in f:
	lineSlice = re.split(r'\W+',line)
	for cha in lineSlice:
		# print(cha)
		if cha not in resultDic:
			resultDic[cha] = 1
		else:
			resultDic[cha]=resultDic.get(cha)+1

tempCount = 1
mostApprearence = ''
for key in resultDic.keys():
	if resultDic[key]>tempCount:
		tempCount = resultDic[key]
		mostApprearence = key

print("'"+key +"' appears for "+str(resultDic[mostApprearence])+" times.")


	
