import os
import sys


path = sys.argv[1]

for filename in os.listdir(path):
	if 'jpg' in filename:
		indx = filename.rindex('.')
		tempname = filename[:indx]
		commandname = "tesseract"+" "+os.path.join(path,filename)+" "+os.path.join(path,tempname)
		os.system(commandname)


