# python 2

import os

a = open("filenames.txt", "w")
for path, subdirs, files in os.walk(r'F:\coverage'):
	for filename in files:
		a.write(filename + '\n')
