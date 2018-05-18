import xlsxwriter
import os,ast

with open("numbers.txt") as f:
	content = ast.literal_eval(f.read())
	workbook = xlsxwriter.Workbook("numbers.xlsx")
	sheet = workbook.add_worksheet("numbers")
	row = 0
	col = 0
	for item in content:
		innercol = col
		for number in item:
			sheet.write(row,innercol,number)
			innercol+=1
		row+=1
	workbook.close()

		