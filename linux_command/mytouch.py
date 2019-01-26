#!/usr/bin/python2

import sys
import os

# this is touch command program 

path = sys.argv[1:]
try:
	def directory():
		for name in path:
			if not os.path.exists(name):
		    		os.makedirs(name)				
			else:
				os.path.exists(name)
		return name
	def files():
		for name in path:
			os.path.exists(name)
			f=open(name,'r+')
			f.close()					
		return name		
	
	files()
	directory()
except (IOError):
	exit()

 
