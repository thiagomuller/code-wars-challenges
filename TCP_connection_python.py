import socket

TCP_IP = '140.211.10.69'
TCP_PORT = 80
BUFFER_SIZE = 1024
Message = """
GET /moin/TcpCommunication HTTP/1.1
Host: wiki.python.org
"""

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_IP,TCP_PORT))
s.send(Message)
data = s.recv(BUFFER_SIZE)
s.close()

print(data)