import socket,sys

#Create a socket

def get_verification(mail,ip,port) :
	try :

		print ip, port,"######################"
		s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)         # Create a socket object

		#host = socket.gethostbyaddr(str(ip))[0]
		host = socket.gethostname()
		print host,"-------------------------"
		port = int(port)               # Reserve a port for your service.
		s.connect((host, port))
		s.send(mail)
		msg = s.recv(1024)

		if msg=="INLIST":
			s.close()
			return False
		elif msg == "NOTINLIST" :
			s.close()
			return True
		else :
			s.close()
			print "Error. Looping Back"
			return get_verification(mail,ip,port)

	except :
		return False

#get_verification("a",sys.argv[1],sys.argv[2])
