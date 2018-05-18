import io

def getFilterWords(fileName):
	with open(fileName) as f:
		return [line.rstrip('\n') for line in f]

def filterInput(wordslist):
	userInput = input()
	if userInput in wordslist:
		print("Freedom")
	else:
		print("Human Rights")



alist = getFilterWords("filter_words.txt")
filterInput(alist)
