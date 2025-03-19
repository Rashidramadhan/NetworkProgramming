import socket


HOST = '127.0.0.1'
PORT = 9090

def start_client():
    """Connects to the server and sends a message."""
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        client_socket.connect((HOST,PORT))
        print("[CONNECTED] Connected to the server!")

        while True:
            message = input("Enter Message(type 'exit' to quit): ")
            if message.lower() == 'exit':
                break
            
            client_socket.sendall(message.encode())
            response = client_socket.recv(1024)
            print(f"[SERVER RESPONSE]: {response.decode()}")
       



if __name__ == "__main__":
    start_client()