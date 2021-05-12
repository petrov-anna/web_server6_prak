import socket

sock = socket.socket()
sock.connect(('localhost', 80))
sock.send("Подключение прошло успешно".encode())

data = sock.recv(1024)
sock.close()

print(data.decode())
