import sys
#with open('NGS43a_H_141105A_ClinEx_1_1407200_135136_S_ATCACG_Exon_GeneLevelRDsummary' + '.csv') as coverageall:
with open(sys.argv[1] + '.csv') as coverageall:
	import csv
	readfile = csv.reader(coverageall, delimiter = '\t')
	line = 0
	for row in readfile:
		#create the output (will append if this exists already)
		if line > 0:
			with open(sys.argv[2] + '.csv', mode='a') as coveragegenes:
				filteredfilewriter = csv.writer(coveragegenes, delimiter='\t', lineterminator='\n')
				filteredfilewriter.writerow(row)                
		#iterate through the loop
		line += 1