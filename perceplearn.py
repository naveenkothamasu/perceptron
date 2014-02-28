import sys;

inputFileName = sys.argv[1];
wordTagMap = {};
inputFile = open(inputFileName, "r");
for line in inputFile:
	prevWord = "START"
	line = line.lower();
	wordTagList = line.split(" ");	
	for word in wordTagList:
		sep = word.find("/");	
		w = word[0:sep];
		t = word[sep+1 : len(word)-1]
		if w in wordTagMap:
			if t in wordTagMap[w]['tags']:
				wordTagMap[w]['tags'][t] += 1;
			else:
				wordTagMap[w]['tags'][t] = 1; 
		else:
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

for word in freqWordTagMap:
	print freqWordTagMap[word]+" ",
	print "w:" + word+" ",
	print "p:" + wordTagMap[word]['prevWord']
