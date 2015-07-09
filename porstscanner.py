import socket
import sys
import datetime
t1 = datetime.now()
ip = raw_input
#Well Known Ports
r1 = 1
r2 = 1025
try:
#kind of like a dictionary for all of the well known ports but faster than making all of them in a tuple
for port in range(r1, r2):
#IPV4 socket and TCP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.setdefaulttimeout(.5)
result = sock.connect_ex((ip, port))
if result == 0:
print "port %d is open"
sock.close()
except socket.error:
print "couldn't connect"
sys.exit
except socket.gaierror:
print "Couldn't resolve hostname"
sys.exit
except KeyboardInterrupt:
sys.exit
t2 = datetime.now()
print "scan finished in" t1-t2 "minutes" 
