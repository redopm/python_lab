#!/usr/bin/python2

import sys
import os

# this is touch command program 

name = sys.argv[1:]
a=os.system("ls")
for i in name :
	if (a == i):
		f=open(i,'a+').close()
		
	else:
		f=open(i,'w+').close()
		





 
