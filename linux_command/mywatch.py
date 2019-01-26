#!/usr/bin/python

import os 
import sys

path = sys.argv[1:]

try:
	for name in path:
		if os.path.exists(name):
			f=open(name,'r+')
			x=f.read()
			f.close()
			print x

except:
	exit()
