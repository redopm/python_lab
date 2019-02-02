#!/usr/bin/python 
import socket
#colling udp mathod
#difining ip and port 
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
# here s is udp type and ipv4 socket
# use the ipv4,type 
ip_addr="192.168.1.46"
port="8888"
conn=(ip_addr,port)
while 4 > 2:

	a=raw_input("enter your data :")

	s.sendto(a,conn)

