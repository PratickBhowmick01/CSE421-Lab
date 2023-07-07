import socket

HEADER = 16
PORT = 5858												# Port address
SERVER = socket.gethostbyname(socket.gethostname())		# IP address
ADDR = (SERVER, PORT)									# Socket address (port+IP)
FORMAT = 'utf-8'										# UTF string format 
DISCONNECT_MESSAGE = 'End'

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 	# sock_stream => use of TCP
server.bind(ADDR)

server.listen()
print('Server Listening.')
conn, addr = server.accept()							# connection + socket addr

connection = True 
while connection: 
	message_length = conn.recv(HEADER)
	if message_length: 					
		message_length = int(message_length) 
		message = conn.recv(message_length).decode(FORMAT)

		if message == DISCONNECT_MESSAGE:
			connection = False
			conn.send('Disconnecting.'.encode(FORMAT))

		else:
			hours = int(message)
			salary = 0

			if hours <= 40: 
				salary = 200*hours
			else: 
				salary = 8000 + 300*(hours-40)
			conn.send(f"Salary: {salary}".encode(FORMAT))

conn.close()