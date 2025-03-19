import socket


HOST = '127.0.0.1'
PORT = 9090

def start_server():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        server_socket.bind((HOST,PORT))
        server_socket.listen()
        print(f"server Listening on {HOST}: {PORT}.....")

        while True:
            try:
                client_socket, client_address = server_socket.accept()
                print(f"Connected by {client_address}")
                with client_socket:
                    data = client_socket.recv(1024).decode()
                    if data:
                        print(f"Received {data}")
                        client_socket.sendall("Message Received!".encode())
            except Exception as e:
                print(f"[ERROR] Exception occurred: {e} ")
                break


if __name__ == "__main__":
    start_server()