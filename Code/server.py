
import socket,sys            # Import socket module



s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)         # Create a socket object
host = socket.gethostname() # Get local machine name
port = int(sys.argv[1])             # Reserve a port for your service.
s.bind((host, port))        # Bind to the port

s.listen(8)                 # Now wait for client connection.




print "Server Started \n"

#Server running on while loop
mail = []
while True:
	# Establish connection with client.
	c, addr = s.accept()
	print 'New connection from', addr
	msg = c.recv(1024) #Recieve the messages
	msg = msg.strip()
	
	if msg in mail :
		response = "INLIST"
	else :
		response = "NOTINLIST"
		mail.append(msg)
	c.send(response)
	# Close the connection once work is done
	c.close()
	print len(mail)
