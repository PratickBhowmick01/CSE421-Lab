import socket

HEADER = 16
PORT = 5858							# Port address
SERVER = socket.gethostbyname(socket.gethostname())		# IP address
ADDR = (SERVER, PORT)						# Socket address (port+IP)
FORMAT = 'utf-8'						# UTF string format 
DISCONNECT_MESSAGE = 'End'

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 	# sock_stream => use of TCP
client.connect(ADDR)


def send_message(message): 
	message = message.encode(FORMAT)
	message_length = len(message) 
	send_length = str(message_length).encode(FORMAT)
	send_length += b' ' * (HEADER - len(send_length))	# empty spaces_padding

	client.send(send_length) 
	client.send(message)

	print(client.recv(2048).decode(FORMAT))	

send_message(f"Client IP: {SERVER}; Client Device Name: {socket.gethostname()}")
send_message(DISCONNECT_MESSAGE)					