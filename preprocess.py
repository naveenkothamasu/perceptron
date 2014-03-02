#!/usr/bin/env python

import sys;
import re;

inputFileName = sys.argv[1];
isDev = "train"
if len(sys.argv) > 2:
	isDev = "dev"
wordTagMap = {};
allTags = {};

inputFile = open(inputFileName, "r");
actuals = open("actuals.txt", "w");
if isDev == "dev":
	mm = open("dev", "w");
else:
	mm = open("train","w");
nextWord = "END";
nnext = "END";
for line in inputFile:
	line = line.replace("\n","");
	prevWord = "START"
	pprev = "START"
	#line = line.lower();
	line = line.replace("#", "HASH");
	wordList = line.split(" ");	
	i = 0;
	for word in wordList:
		if word != "":
			wLen = len(wordList)-2;
			if i == 0:
				prev = "START"
				pprev = "START"
			elif i == 1:
				pprev = "START"
				m = re.search(".+/", wordList[i-1])
				sep = len(m.group(0));
				prev = wordList[i-1][0:sep-1]
			else:		
				m = re.search(".+/", wordList[i-1])
				sep = len(m.group(0));
				prev = wordList[i-1][0:sep-1]
				m = re.search(".+/", wordList[i-2])
				sep = len(m.group(0));
				pprev = wordList[i-2][0:sep-1]
			if i == wLen:
				nextWord = "END"
				nnext = "END"
			elif i == wLen-1:
				nnext = "END"
				m = re.search(".+/", wordList[i+1]);
				sep = len(m.group(0));
				nextWord = wordList[i+1][0:sep-1]
			else:
				m = re.search(".+/", wordList[i+1]);
				sep = len(m.group(0));
				nextWord = wordList[i+1][0:sep-1]
				if wordList[i+2] != "":
					m = re.search(".+/", wordList[i+2]);
					sep = len(m.group(0));
					nnext = wordList[i+2][0:sep-1]
				else:
					nnext = "END"
			m = re.search(".+/", word);
			sep = len(m.group(0));
			w = word[0:sep-1];
			t = word[sep: len(word)]	
			pLen = len(prevWord);
			ppLen = len(pprev);
			cLen = len(w);	
			nLen = len(nextWord);
			nnLen = len(nnext);
			if isDev == "dev":
				mm.write("? ");	
				actuals.write(t+"\n");
			else:
				mm.write(t+" ");
			mm.write("csuf:" + w[cLen-2:cLen]+" ")
			#mm.write("psuf:" + prev[pLen-2:pLen]+" ")
			#mm.write("nsuf:" + nextWord[nLen-2:nLen]+" ")
			#mm.write("nnsuf:" + nnext[nnLen-2:nnLen]+" ")
			#mm.write("pw2:" + pprev+" ")
			mm.write("pw:" + prev+" ")
			mm.write("cw:" + w+" ")
			mm.write("nw:" + nextWord+" ")
			#mm.write("nw2:" + nnext)
			mm.write("\n");
			i += 1;
		
inputFile.close();
mm.close();
actuals.close();
if isDev == "dev":
	print "Generated dev"
	print "Generated actuals.txt"
else:
	print "Generated train"
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

mm = open("megam.train", "w");
for word in freqWordTagMap:
	pLen = len(wordTagMap[word]['prevWord']);
	ppLen = len(wordTagMap[word]['pprev']);
	cLen = len(word);	
	nLen = len(wordTagMap[word]['nextWord']);
	nnLen = len(wordTagMap[word]['nnext']);
	mm.write( freqWordTagMap[word]+" ");
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
print "Generated megam.train"
i=1;
for t in allTags:
	print "s:"+t+":e";
	i=i+1;
print  i;
'''
