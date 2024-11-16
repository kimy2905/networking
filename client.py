import socket
import os
import threading

server_ip = "127.0.0.1"
server_port = 7001
server_address = (server_ip, server_port)

#2 READER FUNCTION
def reader(sock):
    while True:
        try:
            response = sock.recv(1024)
            response = str(response, "UTF-8")
            print(response)
        except:
            print("Client Disconnected")
            os._exit(0)

#1 CONNECTION SET UP 
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    sock.connect(server_address)
    print(f"Connected to Server: {server_address}")

    thread = threading.Thread(target=reader, args=(sock,))
    thread.start()

    name = input("What is your name: ")
    sock.sendall(bytes(f"USER|{name}", "UTF-8"))

#3 INPUT LOOP
    print("Enter your messages to send (type 'exit' to quit):")
    while True:
        message = input()
        if message.lower() == "exit":
            break
        elif message.lower() == "users":
            sock.sendall(bytes("DIR", "UTF-8"))
        else:
            sock.sendall(bytes(f"MSG|{message}", "UTF-8"))

    print("Client closed")
