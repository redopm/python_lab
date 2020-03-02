#!/usr/bin/python

import webbrowser
import pyttsx3



try:
	x=raw_input("enter first number:")
	y=raw_input("enter second number:")
	option='''
	Press 1 for Addition
	Press 2 for Subtraction
	Press 3 for Multiplication
	Press 4 for Division
	'''
	print option
	choice=raw_input("Enter your input :")

	if choice =='1':
		print int(x)+int(y)

	elif choice == "2":
		print int(x)-int(y)

	elif choice =='3':
		print int(x)*int(y)

	elif choice == "4":
		print float(x)/float(y)

except(ZeroDivisionError,NameError,ValueError):
	s="calculator"
	webbrowser.open("https://www.google.com/search?q="+s)
	engine=pyttsx3.init()
	engine.say("tumse na ho payega")
	x=engine.runAndWait()
	print x

finally:
	print "well done!"
		
