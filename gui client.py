import tkinter
import socket
import threading

root = tkinter.Tk()
root.title('Client')
root.wm_state('zoomed')
root.configure(bg='black')
x = root.winfo_screenwidth()
y = 0
y1 = 0
x1 = 25
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((socket.gethostname(), 8967))
username = 'client'


def send_msg(_):
    global x
    global y
    msg = f'{username}>{e.get()}'
    msg = msg.encode('utf-8')
    s.send(msg)
    align = 'ne'
    msg = e.get()
    label = tkinter.Label(text=msg, fg='yellow', bg='black', font=('comicsans', 18))
    if msg == '':
        pass
    else:
        label.place(x=x, y=y, anchor=align)
        e.delete(0, tkinter.END)
        y += 50


def recv_msg():
    global x1
    global y1
    global y
    while True:
        align = 'nw'
        cont = s.recv(1024)
        cont = cont.decode('utf-8')
        if cont.find('>') != -1:
            i = cont.find('>')
            if cont[i + 1:] == '':
                pass
            else:
                y1 = y + 25
                label = tkinter.Label(text=cont, bg='black', fg='white', font=('comicsans', 18))
                label.place(x=0, y=y1, anchor=align)
                y += 50
        elif cont == '':
            pass


e = tkinter.Entry(bg='black', fg='white')
root.bind('<Return>', send_msg)
e.pack()
t = threading.Thread(target=recv_msg)
t.start()
t1 = threading.Thread(target=lambda: send_msg(None))
t1.start()
root.mainloop()
