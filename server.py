import threading
import socket
from queue import Queue
import pickle

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', 5687))
username = 'Ganesh'
conn = socket.socket
l1 = []
adresses = []
connections = []
queue = Queue()


def listening(s1):
    global conn
    global l1
    global adresses
    global connections
    s1.listen(5)
    while True:
        conn, address = s1.accept()
        l1.append(s1)
        print(f'connection from {address} has been established')
        adresses.append(address)
        connections.append(conn)
        print(adresses)
        s1.setblocking(True)
        if len(connections) == 2:
            msg_1 = pickle.dumps(adresses)
            for i in range(0, len(adresses)):
                connections[i].sendto(msg_1, adresses[i])
            recv_msg()


def send_msg():
    while True:
        msg = input()
        msg = list(f'{username}> {msg}')
        msg = pickle.dumps(msg)
        for i in range(0, len(adresses)):
            connections[i].sendto(msg, adresses[i])


def recv_msg():
    while True:
        for i in range(0, len(adresses)):
            msg = connections[i].recv(1024)
            print(msg.decode('utf-8'))
            if i == 0:
                msg = list(msg.decode('utf-8'))
                msg = pickle.dumps(msg)
                connections[1].sendto(msg, adresses[1])
            elif i == 1:
                msg = list(msg.decode('utf-8'))
                msg = pickle.dumps(msg)
                connections[0].sendto(msg, adresses[0])


t = threading.Thread(target=lambda: listening(s))
t.start()
t1 = threading.Thread(target=send_msg)
t1.start()
