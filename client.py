import socket
import threading
import pickle

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((socket.gethostname(), 5687))
username = 'client2'
adresses = []


def recv_mesg(s1):
    global adresses
    sep = ''
    while True:
        msg = s1.recv(1024)
        msg = pickle.loads(msg)
        # msg = sep.join(msg)
        if all(isinstance(n, tuple) for n in msg):
            # print(msg)
            adresses.append(msg)
            print(adresses)
        else:
            msg = sep.join(msg)
            print(msg)


def send_msg(s1):
    while True:
        msg = input()
        msg = f'{username}> {msg}'.encode('utf-8')
        s1.send(msg)
        target = adresses[0][0]
        s1.sendto(msg, target)


t = threading.Thread(target=lambda: recv_mesg(s))
t.start()
t1 = threading.Thread(target=lambda: send_msg(s))
t1.start()
