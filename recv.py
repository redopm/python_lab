#!/usr/bin/python 
import socket
#colling udp mathod
#difining ip and port 
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
# here s is udp type and ipv4 socket
# use the ipv4,type 
ip_addr="0.0.0.0"
port="8888"
#bind ip  and port
s.bind(ip_addr,port)
# buffer size of data
print s.recvfrom(100)

