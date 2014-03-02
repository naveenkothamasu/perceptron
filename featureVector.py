#!/usr/bin/env python

import sys;
import re;

inputFileName = sys.argv[1];
wordTagMap = {};
allTags = {};

inputFile = open(inputFileName, "r");
actuals = open("actuals.dev","w");
mm = open("megam.dev", "w");
nextWord = "END";
nnext = "END";
for line in inputFile:
	line = line.replace("\n","");
	line = line.replace("#", "HASH");
	prevWord = "START"
	pprev = "START"
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
				wordTagMap[w] = { 'tags':{t:1}, 'prevWord': prevWord, 'nextWord': nextWord, 'pprev': pprev, 'nnext': nnext};
			if prevWord in wordTagMap:
				wordTagMap[prevWord]['nextWord'] = w; 
			if pprev in wordTagMap:
				wordTagMap[pprev]['nnext'] = w;
			pprev = prevWord;
			prevWord = w;
			pLen = len(prevWord);
			cLen = len(w);	
			nLen = len(wordTagMap[w]['nextWord']);
			nnLen = len(wordTagMap[w]['nnext']);
			actuals.write( t+"\n");
			mm.write("? ");
			mm.write("csuf:" + w[cLen-2:cLen]+" ")
			mm.write("psuf:" + wordTagMap[w]['prevWord'][pLen-2:pLen]+" ")
			mm.write("nsuf:" + wordTagMap[w]['nextWord'][nLen-2:nLen]+" ")
			mm.write("nnsuf:" + wordTagMap[w]['nnext'][nnLen-2:nnLen]+" ")
			mm.write("pw2:" + wordTagMap[w]['pprev']+" ")
			mm.write("pw:" + wordTagMap[w]['prevWord']+" ")
			mm.write("cw:" + w+" ")
			mm.write("nw:" + wordTagMap[w]['nextWord']+" ")
			mm.write("nw2:" + wordTagMap[w]['nnext'])
			mm.write("\n");
inputFile.close();
mm.close();
actuals.close();
print "Generated megam.dev"
print "Generated actuals.dev"
'''
for word in wordTagMap:
	print word +" ",
	for tag in wordTagMap[word]['tags']:
		print tag + " ",
	print "p:",
	print wordTagMap[word]['prevWord']
freqWordTagMap = {};
for word in wordTagMap:
	mostFreqTagCount = 0;
	mostFreqTag = "";
	for tag in wordTagMap[word]['tags']:
		if mostFreqTagCount < wordTagMap[word]['tags'][tag]:
			mootFreqTagCount = wordTagMap[word]['tags'][tag];
			mostFreqTag = tag;
	freqWordTagMap[word] = mostFreqTag; 
actuals = open("actuals.dev","w");
mm = open("megam.dev", "w");
for word in freqWordTagMap:
	pLen = len(wordTagMap[word]['prevWord']);
	cLen = len(word);	
	nLen = len(wordTagMap[word]['nextWord']);
	nnLen = len(wordTagMap[word]['nnext']);
	actuals.write( freqWordTagMap[word]+"\n");
	mm.write("? ");
	mm.write("csuf:" + word[cLen-2:cLen]+" ")
	mm.write("psuf:" + wordTagMap[word]['prevWord'][pLen-2:pLen]+" ")
	mm.write("nsuf:" + wordTagMap[word]['nextWord'][nLen-2:nLen]+" ")
	mm.write("nnsuf:" + wordTagMap[word]['nnext'][nnLen-2:nnLen]+" ")
	mm.write("pw2:" + wordTagMap[word]['pprev']+" ")
	mm.write("pw:" + wordTagMap[word]['prevWord']+" ")
	mm.write("cw:" + word+" ")
	mm.write("nw:" + wordTagMap[word]['nextWord']+" ")
	mm.write("nw2:" + wordTagMap[word]['nnext'])
	mm.write("\n");
mm.close();
actuals.close();
print "Generated megam.dev"
print "Generated actuals.dev"
i=1;
for t in allTags:
	print "s:"+t+":e";
	i=i+1;
print  i;
'''
