import sys;

actuals = open(sys.argv[1], "r");
results = open(sys.argv[2], "r");
correctTags = 0;
totalTags = 0;
for line in actuals:
	resultsLine = results.readline();
	resultsLine = resultsLine.replace("\n","");
	resultsLine = resultsLine.strip();
	line = line.replace("\n", "");
	line = line.strip();
	totalTags += 1;
	if line == resultsLine:
		correctTags +=1; 
actuals.close();
results.close();

print correctTags;
print totalTags;
print correctTags/totalTags;
