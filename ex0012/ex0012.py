import io

def getFilterWords(fileName):
	with open(fileName) as f:
		return [line.rstrip('\n') for line in f]

def riverCrab(wordslist):
	userInput = input()
	for word in wordslist:
		if word in userInput:
				print(userInput.replace(word,'*' * len(word)))



alist = getFilterWords("filter_words.txt")
riverCrab(alist)