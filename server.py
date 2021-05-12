import datetime
import os
import socket

sock = socket.socket()

try:
    sock.bind(('', 80))
    print("Using port 80")
except OSError:
    sock.bind(('', 8080))
    print("Using port 8080")

sock.listen(5)

conn, addr = sock.accept()
print("Connected", addr)

data = conn.recv(8192)
msg = data.decode()

print(msg)
file_name = str(input("Введите название файла: "))

if file_name != "" and file_name is not None:
    with open(str(file_name)) as file:
        text = file.read()
        location = os.path.abspath(file_name)
else:
    with open("index.html") as file:
        print("Файл по умолчанию -> index.html")
        location = os.path.abspath('index.html')
        text = file.read()

file = str(file)
a = file.find("name=")
b = file.find("mode")
name_file = file[a:b]
c = name_file.find(".")

type_file = name_file[c+1:-2]
date = datetime.datetime.now()
length = len(text)

resp = """HTTP/1.1 200 OK
Server: localhost 
Current date: """ + str(date) + """
Content-type: text/""" + str(type_file) + """ 
Content-length: """ + \
       str(length) + """
Location: """ + str(location) + """
Connection: close
_______TEXT______
""" + text

conn.send(resp.encode())

conn.close()
