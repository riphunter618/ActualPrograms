import tkinter
import socket
import threading

root = tkinter.Tk()
root.title('Server')
root.configure(bg='black')
root.wm_state('zoomed')
x = root.winfo_screenwidth()
y = 0
x1 = 0
y1 = 25

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
username = 'Ganesh'
s.bind((socket.gethostname(), 8967))
s.listen(1)
conn, address = s.accept()
print(f'connection from {address} has been established')


def send_msg(_):
    global x
    global y
    cont = f'{username}>{e.get()}'
    cont = cont.encode('utf-8')
    conn.send(cont)
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
        msg = conn.recv(1024)
        msg = msg.decode('utf-8')
        if msg.find('>') != -1:
            i = msg.find('>')
            if msg[i + 1:] == '':
                pass
            else:
                y1 = y + 25
                label1 = tkinter.Label(text=msg, bg='black', fg='white', font=('comicsans', 18))
                label1.place(x=0, y=y1, anchor=align)
                y += 50
        elif msg == '':
            pass


e = tkinter.Entry(bg='black', fg='white')
root.bind('<Return>', send_msg)
e.pack()
t = threading.Thread(target=recv_msg)
t.start()
t1 = threading.Thread(target=lambda: send_msg(None))
t1.start()
root.mainloop()
