#!/usr/bin/env python

import sys;
import re;

inputFileName = sys.argv[1];
wordTagMap = {};
allTags = {};

inputFile = open(inputFileName, "r");
for line in inputFile:
	line = line.replace("\n","");
	prevWord = "START"
	line = line.lower();
	wordTagList = line.split(" ");	
	for word in wordTagList:
		if word != "":
			m = re.search(".+/",word);	
			sep = len(m.group(0));
			w = word[0:sep] 
			t = word[sep : len(word)]
			if w in wordTagMap:	
				if t in wordTagMap[w]['tags']:
					wordTagMap[w]['tags'][t] += 1;
				else:
					wordTagMap[w]['tags'][t] = 1; 
			else:
				allTags[t] = 0;
				wordTagMap[w] = { 'tags':{t:1}, 'prevWord': prevWord};
			prevWord = w;
inputFile.close();
'''
for word in wordTagMap:
	print word +" ",
	for tag in wordTagMap[word]['tags']:
		print tag + " ",
	print "p:",
	print wordTagMap[word]['prevWord']
'''
freqWordTagMap = {};
for word in wordTagMap:
	mostFreqTagCount = 0;
	mostFreqTag = "";
	for tag in wordTagMap[word]['tags']:
		if mostFreqTagCount < wordTagMap[word]['tags'][tag]:
			mootFreqTagCount = wordTagMap[word]['tags'][tag];
			mostFreqTag = tag;
	freqWordTagMap[word] = mostFreqTag; 
'''
for word in freqWordTagMap:
	print freqWordTagMap[word]+" ",
	print "w:" + word+" ",
	print "p:" + wordTagMap[word]['prevWord']
'''
for t in allTags:
	print "s:"+t+":e";
