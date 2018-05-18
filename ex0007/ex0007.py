import glob,os

for pyfile in glob.glob("*.py"):
	commentLines = 0
	spaceLines = 0
	codeLines = 0
	for line in open(pyfile,'r'):
		if line.startswith("#"):
			commentLines+=1
		elif line.isspace():
			spaceLines+=1
		else:
			codeLines+=1
	print("In '"+ pyfile+"' ,there are comment lines: " + str(commentLines)+ " ,space lines: " + str(spaceLines)+ " ,code lines: " + str(codeLines))
