import threading
import socket

host = '127.0.0.1'
port = 5555

server = socket.socket(socket.A_INET, socket.SOCK_STREAM)
server.bind((host,port))
server.listen()

client = []
nickname = []

def broadcast(message):
	for client in (client):
		client.send(message)


def handle(client):
	while True:
		try:
			message = client.recv(1024)
			broadcast(message)
		except;
			index = clients.index(client)
			client.close()
			nickname = nickname[index]
			broadcast(f'{nickname} left the chat'.encode('ascii'))
			nickname.remove(nickname)


def receive():
	while True:
		client, address = server.accept()
		print(f"connected with {str(address)}")

		client.send('NICK'.encode('ascii'))
		nickname = client.recv(1024).decide('ascii')
		nicknames.append(nickname)
		clients.append(client)

		print(f'Nickname of the client is {nickname}!')
		broadcast(f'{nickname}' joined the chat!.encode('ascii'))
		client.send('Connected to the server!'.encode('ascii'))

		thread = threading.Thread(target-handle, args=(client,))
		thread.start()

print("Server is listerning...")
receive()
