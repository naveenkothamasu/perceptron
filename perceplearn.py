import sys;

inputFileName = sys.argv[1];
i = 0;
iterations = 3;
for cmd in sys.argv:
	if cmd == '-i':
		iterations = int(sys.argv[i+1]);	
	i += 1;
		
categoryWeights = {'SPAM':{},  'HAM':{}};
avgCategoryWeights = {'SPAM':{}, 'HAM':{}};
inputList = [];
wordMap = {};

inputFile = open(inputFileName, "r");
for line in inputFile:
	inputList += [line]
inputFile.close();
for line in inputList:
	line = line.replace("\n", "");
	wordList = line.split(" ");
	wordList.remove(wordList[0]);
	for word in wordList:
		if word != " ":
			word = word.strip();
			if word in wordMap:
				wordMap[word] += 1;
			else:
				categoryWeights["SPAM"][word] = 0;	
				categoryWeights["HAM"][word] = 0;	
				avgCategoryWeights["SPAM"][word] = 0;
				avgCategoryWeights["HAM"][word] = 0;	
				wordMap[word] = 1;

def initCategoryWeights(categoryWeights):
	for category in categoryWeights:
		for word in categoryWeights[category]:
			categoryWeights[category][word] = 0;
def addCategoryWeights():
	for category in categoryWeights:
		for word in categoryWeights[category]:
			avgCategoryWeights[category][word] += categoryWeights[category][word];

def printWeights(categoryWeights):
	for category in categoryWeights:
		for word in categoryWeights[category]:
			print str(categoryWeights[category][word])+"\t",
		print "";
	print "";
currentSum = 0;
for category in categoryWeights:
	print "------------------------------------------------------";
	for word in categoryWeights[category]:
			print word+"\t",
	print "";
	break;
initCategoryWeights(avgCategoryWeights);
printWeights(categoryWeights);	
i = 0;
initCategoryWeights(categoryWeights);
while i < iterations:
	for line in inputList: 
		line = line.replace("\n", "");
		vector = line.split(" ");
		wordList = line.split(" ");
		y = vector[0];
		vector.remove(y);
		maximum = -1;
		resCat = "";
		for category in categoryWeights:
			for word in vector:
				currentSum += categoryWeights[category][word];
			if(maximum <= currentSum):
				maximum = currentSum;
				resCat = category;
		if resCat != y:
			for category in categoryWeights:
				if category != y:
					for word in vector:	
						categoryWeights[category][word] -= 1; 
				else:
					for word in vector:	
						categoryWeights[category][word] += 1;
		printWeights(categoryWeights);	
	addCategoryWeights();	
	i += 1;
printWeights(avgCategoryWeights);
for category in categoryWeights:
	print "------------------------------------------------------";
	for word in categoryWeights[category]:
			print word+"\t",
	print "";
	break;
