import xlsxwriter,xlrd
import os,ast
def writeDicContent(txtName,xlsxName,sheetName):
		with open(txtName) as f:
			workbook = xlsxwriter.Workbook(xlsxName)
			sheet = workbook.add_worksheet(sheetName)
			content = ast.literal_eval(f.read())
			row = 0
			col = 0
			for item in content.items():
				sheet.write(row,col,item[0])
				innercol = col
				if type(item[1]) is list:
					for value in item[1]:
						innercol+=1
						sheet.write(row,innercol,value)
				elif type(item[1]) is str:
					innercol+=1
					sheet.write(row,innercol,item[1])
				row+=1
				
			workbook.close()


writeDicContent("students.txt","students.xlsx","students")
writeDicContent("cities.txt","cities.xlsx","cities")


	



