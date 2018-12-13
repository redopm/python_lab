#!/usr/bin/python
import webbrowser
import os
import subprocess


options='''
press  1  to  open default web browser :   
press  2  to  check currnet logined user  :   
press  3  to ask user input  and search in google  :   
press  4  to  check number of tabs in your web browser :   
press  5  to  logout your system graphically  :   
press  6  to  login  facebook account  :   
press  7  to send email to someone  :   
press  8  to list all connected ip and mac in your current network  :  
''' 
print options 
choice=raw_input()
# put your if else code here 
print choice ,type(choice)

if choice =='1':
	webbrowser.open("https://www.google.com")

elif choice == "2":
	os.system("whoami")

elif choice =='3':
	s=raw_input("search on goole:")
	webbrowser.open_new_tab("https://www.google.com/search?q="+s)

elif choice == "5":
	subprocess.call(["logout"])
#elif choice == "4":
elif choice == "6":
	webbrowser.open_new_tab("https://www.facebook.com/")
	
elif choice =="7":
	raw_input("enter your email id :")
	print "sorry we are working on this"

elif choice == "8":


#else:
	print "selection wrong!"
             
