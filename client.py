import socket


HOST = '127.0.0.1'
PORT = 9090

def start_client():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        client_socket.connect((HOST,PORT))
        client_socket.sendall("Hello Server, I am  the Client!!".encode())
        response = client_socket.recv(1024).decode()
        print(f"Server Response: {response}")
        client_socket.close()



if __name__ == "__main__":
    start_client()