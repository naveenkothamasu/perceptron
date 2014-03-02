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
if isDev == "dev":
	actuals = open("actuals.txt", "w");
        mm = open("dev", "w");
else:
        mm = open("train","w");
for line in inputFile:
	line = line.replace("\n","");
	line = line.lower();
	line = line.replace("#", "HASH");
	
	wordList = line.split(" ");
	i = 0;
	for word in wordList:
		if word != "":	
			wLen = len(wordList)-1;
			if i == 0:
				prev = "START"
				pprev = "START"
			elif i == 1:
				pprev = "START";
				temp = wordList[i-1];
				m = re.search(".+/", temp);
				sep2 = len(m.group(0));
				part = temp[0:sep2-1];
				m = re.search(".+/", part);
				sep1 = len(m.group(0));
				prev =  temp[0:sep1-1]
			else:	
				#prevword
				temp = wordList[i-1];
				m = re.search(".+/", temp);
				sep2 = len(m.group(0));
				part = temp[0:sep2-1];
				m = re.search(".+/", part);
				sep1 = len(m.group(0));
				prev =  temp[0:sep1-1]
				
				#pprev
				temp =wordList[i-2];
				m = re.search(".+/", temp);
				sep2 = len(m.group(0));
				part = temp[0:sep2-1];
				m = re.search(".+/", part);
				sep1 = len(m.group(0));
				pprev =  temp[0:sep1-1]

			#-------------next words------------------

			if i == wLen:
				nextWord = "END";
				nnext = "END";
			elif i == wLen-1:
				nnext = "END"	
				#next
				temp = wordList[i+1];
				if temp != "":
					m = re.search(".+/", temp);
					sep2 = len(m.group(0));
					part = temp[0:sep2-1];
					m = re.search(".+/", part);
					sep1 = len(m.group(0));
					nextWord =  temp[0:sep1-1]
				else:
					nextWord = "END"
			else:
				#next
				temp = wordList[i+1];
				m = re.search(".+/", temp);
				sep2 = len(m.group(0));
				part = temp[0:sep2-1];
				m = re.search(".+/", part);
				sep1 = len(m.group(0));
				nextWord =  temp[0:sep1-1]
				
				#nnext
				temp = wordList[i+2];
				if temp != "":
					m = re.search(".+/", temp);
					sep2 = len(m.group(0));
					part = temp[0:sep2-1];
					m = re.search(".+/", part);
					sep1 = len(m.group(0));
					nnext =  temp[0:sep1-1]
				else:
					nnext = "END";
				
			#----------- current word ------------------
			m = re.search(".+/", word);
			sep2 = len(m.group(0));
			part = word[0:sep2-1];
			m = re.search(".+/", part);
			sep1 = len(m.group(0));
			#print word[0:sep1-1]+" ",
			#print word[sep1:sep2-1]+" ",
			#print word[sep2: len(word)]
			w = word[0:sep1-1];	
			t = word[sep2:len(word)];
			pLen = len(prev);
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
	                mm.write("psuf:" + prev[pLen-2:pLen]+" ")
	                mm.write("nsuf:" + nextWord[nLen-2:nLen]+" ")
	               	#mm.write("nnsuf:" + nnext[nnLen-2:nnLen]+" ")
	                mm.write("pw2:" + pprev+" ")
	                mm.write("pw:" + prev+" ")
	                mm.write("cw:" + w+" ")
	                mm.write("nw:" + nextWord+" ")
	                #mm.write("nw2:" + nnext)
	                mm.write("\n");
			i = i+1;
				
inputFile.close();
mm.close();
if isDev == "dev":
	actuals.close();
        print "Generated dev"
        print "Generated actuals.txt"
else:
        print "Generated train"

			
