#!/usr/bin/python

import os,sys

try:
	path=sys.argv[1:]
	cd=os.getcwd()
	for name in path:
		os.chdir(name)
		print(os.getcwd())
	

except(OSError):
	print name+":No such file or directory"
