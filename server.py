import socket
import sys
import os
from termcolor import *

def create_socket():
    try:
        global host
        global port
        global s
        host = ''
        port = 8888
        s = socket.socket()
        print(colored("Connection Created Successfully","light_green",attrs=["bold"]))
    
    except socket.error as msg:
        print(colored(f'Socket Connection Error {msg}',"red",attrs=["dark"]))


def bind_socket():
    try:
        global host
        global port
        global s
        print(colored(f"Binding the port: {port}","yellow"))
        s.bind((host,port))
        s.listen(5)

    except socket.error as msg:
        print(colored(f"Socket Binding Error {msg} \n Retrying...","red"))
        bind_socket()


def socket_accept():
    conn, address = s.accept()
    print(colored(f"Connection has Been Established with {address[0]}  at port  {address[1]}",'green'))
    send_command(conn)
    conn.close()

def send_file(filename,conn_):
    f = open(filename,"rb")
    data = f.read(1024)
    while data:
        conn_.sendall(data.encode())
    conn_.sendall(b'End of File Transfer')

def send_message(msg,conn_):
    conn_.sendall(msg.encode())
        
def exec_cmd(cmd,conn_):
    result = os.popen(cmd).read()
    conn_.sendall(result.encode())

def send_command(conn):
    while True:
        send_ = input("Enter The Message to Send: ")
        if send_ == "quit":
            conn.send(str.encode("Connection has been closed"))
            conn.close()
            break
        elif send_.startswith('file:'):
            send_message('FILE TRANSFER',conn)
            send_file(send_[5:],conn)
        elif send_[:3] == 'cmd:':
            send_message('CMD EXEC',conn)
            exec_cmd(send_[4:],conn)
        else:
            send_message(send_,conn)
        msg_ = str(conn.recv(1024),"utf-8")
        print(colored(f"Client:  {msg_}",'cyan'))

def main():
    create_socket()
    bind_socket()
    socket_accept()

if __name__ == '__main__':
    main()


