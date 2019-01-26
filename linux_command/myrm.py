#!/usr/bin/python

import os,sys

path=sys.argv[1:]
try:
	def removd():
		for name in path:
			if not os.path.exists(name):
		    		print "No such file or directory: "+name
			else:
				os.path.exists(name)
				os.rmdir(name)
		return name

	removd()
except(OSError):
	exit()
