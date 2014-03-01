import sys;

inputFileName = sys.argv[1];

inputFile = open(inputFileName, "r");
results = open("results.txt", "w");

for line in inputFile:
	wordList = line.split("\t");
	results.write(wordList[0]+"\n");

print "Generated results.txt"
