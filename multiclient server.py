import threading
import socket
from queue import Queue
import _thread

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(), 5687))
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
        _thread.start_new_thread(recv_msg, (conn, ))
        adresses.append(address)
        connections.append(conn)
        print(adresses)
        print(connections)
        # recv_msg()


def send_msg():
    while True:
        msg = input()
        msg = f'{username}> {msg}'.encode('utf-8')
        # msg = pickle.dumps(msg)
        for i in range(0, len(adresses)):
            connections[i].sendto(msg, adresses[i])


def recv_msg(connection):
    while True:
        msg = connection.recv(1024)
        print(msg.decode('utf-8'))
        print(connection)
        # if i == 0:
        #     connections[1].sendto(msg, adresses[1])
        # elif i == 1:
        #     connections[0].sendto(msg, adresses[0])


t = threading.Thread(target=lambda: listening(s))
t.start()
t1 = threading.Thread(target=send_msg)
t1.start()
# t2 = threading.Thread(target=recv_msg)
# t2.start()
