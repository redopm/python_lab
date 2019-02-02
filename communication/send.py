#!/usr/bin/env  python2
import  socket
import thread
from time import sleep
def sender():


	#  calling  udp method
	#                       ipv4 ,        UDP type 
	s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
	#  here s  is udp  type with  ipv4  socket 
	#  defining  ip and port  for comm
	ip_addr="192.168.1.46"
	port=8888

	while 4 >  2 :

		data=raw_input("enter your data :  ")
		s.sendto(data,(ip_addr,port))
		print s.recvfrom(100)

def recv():
	s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
	#  here s  is udp  type with  ipv4  socket 
	#  defining  ip and port  for comm
	ip_addr="0.0.0.0"
	port=8888

	conn=(ip_addr,port)
	# binding  ip  and port 
	s.bind(conn)
	#          data buffer size rec from  per client/sender  
	while True:
		data=s.recvfrom(100)
		print  "--->>"+data[0]+"   from client IP "+data[1][0]
		r=raw_input("type your rply :  ")
	s.sendto(r,data[1])	

thread.start_new_thread(sender,())
thread.start_new_thread(recv,())
while True:
	pass
