#!/usr/bin/python
import socket 
import sys


host = raw_input("enter site: ") 
try:
	s = socket.gethostbyname_ex( host ) 
except socket.gaierror:
	print "domain couldn't be found" 
sys.exit

print s
