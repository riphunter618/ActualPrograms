import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('192.168.0.10', 7899))
s.listen(1)
conn, address = s.accept()
path = 'C:\\Users\\Ganesh\\PycharmProjects\\untitled6\\k.py'
with open(path, 'rb') as f:
    cont = f.read()
    conn.send(cont)
