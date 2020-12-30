import socket
import threading

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((socket.gethostname(), 5687))
username = 'client2'


def recv_mesg(s1):
    while True:
        msg = s1.recv(1024).decode('utf-8')
        if type(msg) == str:
            print(msg)


def send_msg(s1):
    while True:
        msg = input()
        msg = f'{username} > {msg}'.encode('utf-8')
        s1.send(msg)


t = threading.Thread(target=lambda: recv_mesg(s))
t.start()
t1 = threading.Thread(target=lambda: send_msg(s))
t1.start()
