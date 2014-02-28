#!/usr/bin/env python

import sys;
import re;

inputFileName = sys.argv[1];

inputFile = open(inputFileName, "r");
outputFile = open("fetures.txt","w");
for line in inputFile:
	newline = "";
	line = line.lower();
	line = line.replace("\n","");
	wordList = line.split(" ");
	for word in wordList:
		if word != "" :
			m = re.search(".+/",word);
			w = m.group(0);
			tag = word[len(m.group(0)):len(word)];
			newline += w.replace("/", " ");

	outputFile.write(newline+"\n");

inputFile.close();
outputFile.close();
print "generated features.txt"

	

		
