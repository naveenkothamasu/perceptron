#!/usr/bin/env python
import sys;
import fileinput;

modelfile = open(sys.argv[1], "r");
line = modelfile.readline();
line = line.replace("\n", "");
wordList = line.split("\t");
modelfileDict = {};
wordList.remove(wordList[0]);
allCategories = [];
i=0;
for word in wordList:
	if word != "":
		allCategories.append(word);

for line in modelfile:
	if i < 1:
		i += 1;
		continue;
	tempList= [];
	wordList = line.split("\t");
	tempList.append(wordList[1]);
	tempList.append(wordList[2]);
	modelfileDict[wordList[0].strip()] = tempList;
modelfile.close();
print allCategories;
for line in sys.stdin:
	maxWgt = -sys.maxint;
	curWgt = 0;
	predicted = "";
	wordList = line.split();
	i = 0;
	for category in allCategories:
		for word in wordList:
			if word in modelfileDict:
				curWgt += int(modelfileDict[word][i]);
		if maxWgt < curWgt:
			maxWgt = curWgt;
			predicted = category;
		i += 1;
print predicted;
