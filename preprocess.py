#!/usr/bin/env python

import sys;
import re;

inputFileName = sys.argv[1];
wordTagMap = {};
allTags = {};

inputFile = open(inputFileName, "r");
nextWord = "";
for line in inputFile:
	line = line.replace("\n","");
	prevWord = "START"
	line = line.lower();
	wordTagList = line.split(" ");	
	for word in wordTagList:
		if word != "":
			m = re.search(".+/",word);	
			sep = len(m.group(0));
			w = word[0:sep-1] 
			t = word[sep : len(word)]
			if w in wordTagMap:	
				if t in wordTagMap[w]['tags']:
					wordTagMap[w]['tags'][t] += 1;
				else:
					wordTagMap[w]['tags'][t] = 1; 
			else:
				allTags[t] = 0;
				wordTagMap[w] = { 'tags':{t:1}, 'prevWord': prevWord, 'nextWord': nextWord};
			if prevWord in wordTagMap:
				wordTagMap[prevWord]['nextWord'] = w; 
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

mm = open("megam.train", "w");
for word in freqWordTagMap:
	pLen = len(wordTagMap[word]['prevWord']);
	cLen = len(word);	
	nLen = len(wordTagMap[word]['nextWord']);
	mm.write( freqWordTagMap[word]+" ");
	mm.write("prev_suf:" + wordTagMap[word]['prevWord'][pLen-2:pLen]+" ")
	mm.write("cur_suf:" + word[cLen-2:cLen]+" ")
	mm.write("next_suf:" + wordTagMap[word]['nextWord'][nLen-2:nLen]+" ")
	mm.write("prev_word:" + wordTagMap[word]['prevWord']+" ")
	mm.write("current_word:" + word+" ")
	mm.write("next_word:" + wordTagMap[word]['nextWord'])
	mm.write("\n");
mm.close();
print "Generated megam.train"
'''
i=1;
for t in allTags:
	print "s:"+t+":e";
	i=i+1;
print  i;
'''
