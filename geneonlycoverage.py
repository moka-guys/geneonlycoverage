#python2
#
# arguments:
# Total coverage output filename without extension
# Gene coverage output filename without extension

import sys
with open(sys.argv[1] + '.csv') as coverageall:
	import csv
	readfile = csv.reader(coverageall, delimiter = '\t')
	line = 0
	for row in readfile:
		#create the output (will overwrite if this exists already) and write the header row to it, adding sample field
		if line < 1 :
			with open(sys.argv[2] + '.csv', mode='w') as coveragegenes:
				filteredfilewriter = csv.writer(coveragegenes, delimiter='\t', lineterminator='\n')
				row.append('Sample')
				filteredfilewriter.writerow(row)          
		#append only the gene coverage rows to the output
		if line > 0 and row[4] == 'Whole gene':
			with open(sys.argv[2] + '.csv', mode='a') as coveragegenes:
				filteredfilewriter = csv.writer(coveragegenes, delimiter='\t', lineterminator='\n')
				row.append(sys.argv[2])
				filteredfilewriter.writerow(row)                
		#iterate through the loop
		line += 1
