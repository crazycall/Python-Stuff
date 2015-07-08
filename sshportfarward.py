import socket
import paramiko 
import threading 
import sys

class Server (paramiko.ServerInerface):
	def _init_(self):
		self.event= threading.Event() 
	def check_channel_request(self,kind,chanid): 
	if kind == 'session': 
		return paramiko.OPEN_SUCCEEDED
	def check_password(self, username, password): 
		if (username == '') and (pasword == ''): 
			return paramiko.AUTH_SUCCESSFUL
		return paramiko.AUTH_FAILED
	server = sys.argv[1] 
	ssh_port = 22
	try: 
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) 
		s.bind ((server, ssh_port)) 
		s.listen(100)
		print 'listening for connection'
		client, addr = s.accept() 
	except Exception, e:	
		print 'Listen failed' + str(e) 
		sys.exit 
	print ' got a connection' 
	
	try:
	Session = paramiko.Transport(client) 
		Session.add_server_key(host_key)
		server = Server() 
	try: 
		Session.start_server(server=server) 
	except paramiko.SSHException, x:
		print '[-] SSH negot failed' 
	channel = session.accept(20) 
	print 'Authenticated'
	print channel.recv(1024) 
	channel.send('Welcome') 
	while True: 
		try:
			command = raw_input("Enter command:") 
			if command != 'exit': 
			channel.send(command) 
			print chan.recv(1024) + 'n' 
		else: 	
			chan.send('exit') 
			print 'exiting' 
			session.exit 
	except Exception, a: 
		print '[-] Caught exception:' + str(a) 
		try: 
			session.exit 
		except: 
			pass	
			sys.exit()
		
