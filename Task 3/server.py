import socket
import threading

HEADER = 16
PORT = 5858							# Port address
SERVER = socket.gethostbyname(socket.gethostname())		# IP address
ADDR = (SERVER, PORT)						# Socket address (port+IP)
FORMAT = 'utf-8'						# UTF string format 
DISCONNECT_MESSAGE = 'End'

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 	# sock_stream => use of TCP
server.bind(ADDR)

server.listen()
print('Server Listening.')


def clients(conn, addr):
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
				count = 0
				v = 'aeiouAEIOU'
				for i in message: 
					if i in v:
						count += 1

				if count == 0: 
					conn.send('Not enough vowels.'.encode(FORMAT))
				elif count <= 2: 
					conn.send('Enough vowels I guess.'.encode(FORMAT))
				else:
					conn.send('Too many vowels.'.encode(FORMAT))

	conn.close()
	

while True: 
	conn, addr = server.accept()
	thread = threading.Thread(target = clients, args = (conn, addr))
	thread.start()
	print(f'Total Clients: {threading.active_count()-1}')		