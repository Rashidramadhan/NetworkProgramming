import socket
import select

HOST = '127.0.0.1'
PORT = 9090
MAX_CONNECTIONS = 10  # Max clients that can connect

def start_server():
    """Starts the server using select for non-blocking I/O."""
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind((HOST, PORT))
    server_socket.listen(MAX_CONNECTIONS)
    server_socket.setblocking(False)  # Set socket to non-blocking mode

    sockets_list = [server_socket]  # List of sockets to monitor
    clients = {}  # Dictionary to store client sockets and addresses

    print(f"Server listening on {HOST}:{PORT}...")

    while True:
        # Use select to check for ready sockets
        readable, _, exceptional = select.select(sockets_list, [], sockets_list)

        for sock in readable:
            if sock == server_socket:
                # Accept new connection
                client_socket, client_address = server_socket.accept()
                client_socket.setblocking(False)
                sockets_list.append(client_socket)
                clients[client_socket] = client_address
                print(f"New connection from {client_address}")
            else:
                # Handle incoming message
                try:
                    message = sock.recv(1024).decode()
                    if message:
                        print(f"Received from {clients[sock]}: {message}")
                        sock.sendall("Message Received!".encode())
                    else:
                        # Client disconnected
                        print(f"Client {clients[sock]} disconnected")
                        sockets_list.remove(sock)
                        del clients[sock]
                        sock.close()
                except Exception as e:
                    print(f"Error with client {clients[sock]}: {e}")
                    sockets_list.remove(sock)
                    del clients[sock]
                    sock.close()

        # Handle exceptions
        for sock in exceptional:
            print(f"Exception with client {clients[sock]}")
            sockets_list.remove(sock)
            del clients[sock]
            sock.close()

if __name__ == "__main__":
    start_server()
