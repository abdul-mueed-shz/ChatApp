import socket
import threading
import time
import pickle

host = socket.gethostbyname(socket.gethostname())
port = 12334

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host, port))

clientle = {}

s.listen()


def clientThread(conn):
    while True:
        try:
            message = conn.recv(2048)
            for client in clientle:
                client.send(message)
        except:
            conn.close()
            del clientle[conn]
            for client in clientle:
                if client != conn:
                    message = username + ' has left the room'
                    client.send(message.encode())
            break

while True:
    print('Waiting For Users')
    conn, addr = s.accept()
    print('Chat Room Active')
    username = conn.recv(2048).decode()
    clientle[conn] = username
    print(clientle)

    for client in clientle:
        if client != conn:
            message = username + ' has entered the room'
            client.send(message.encode())

    threading.Thread(target = clientThread, args= (conn, )).start()
