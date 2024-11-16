import socket
import threading

server_ip = "127.0.0.1"
server_port = 7001
server_address = (server_ip, server_port)

clients = {}
clients_lock = threading.Lock()

#BROADCAST 
def broadcast(message, sender_conn):
    with clients_lock:
        sender_user = clients.get(sender_conn, "Unknown")
        formatted_message = f"{sender_user}: {message}"
        for client_conn in clients:
            if client_conn != sender_conn:
                client_conn.sendall(bytes(formatted_message, "UTF-8"))

# 2 CLIENT CONNECT
def client_connect(connection, address):
    with clients_lock:
        clients[connection] = f"User-{address[1]}"

    while True:
        try:
            data = connection.recv(1024)
            data = str(data, "UTF-8")
            print(f"Received: {data}")
            parts = data.split("|")

            if len(parts) == 2:
                command, content = parts[0], parts[1]
                if command == "USER":
                    with clients_lock:
                        clients[connection] = content
                    connection.sendall(bytes("USER_OK", "UTF-8"))
                elif command == "MSG":
                    broadcast(content, connection)
                    connection.sendall(bytes("MSG_OK", "UTF-8"))
                else:
                    connection.sendall(bytes("NOK", "UTF-8"))
    #3 DIR
            elif data == "DIR":
                with clients_lock:
                    user_list = ", ".join(clients.values())
                connection.sendall(bytes(f"Users logged in: {user_list}", "UTF-8"))
            else:
                connection.sendall(bytes("NOK", "UTF-8"))
        except:
            break

    print(f"Client Disconnected: {address}")
    with clients_lock:
        del clients[connection]
    connection.close()

# 1 START SERVER FUCTION
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
    server_socket.bind(server_address)
    server_socket.listen()
    print(f"Server started at {server_address}")

    while True:
        connection, address = server_socket.accept()
        print(f"Client connected: {address}")
        threading.Thread(target=client_connect, args=(connection, address)).start()
