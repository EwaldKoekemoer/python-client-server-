import socket

DISCONNECT_MSG = ("DISCONNECT")
FORMAT = ("utf-8")
HEADER = 64
PORT = 5050
SERVER = "192.168.8.106"
ADDR = (SERVER ,PORT)

client = socket.socket(socket.AF_INET ,socket.SOCK_STREAM)
client.connect(ADDR)

def send(msg)
    message = msg.encode(FORMAT)
    