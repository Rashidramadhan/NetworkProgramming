import socket
import threading


HOST = '127.0.0.1'
PORT = 9090



'''the two methods bellow are for TCP connection with threading multpiplexing'''
def handle_client(client_socket, client_address):
    """Handles a single client connection."""
    print(f"Connected by {client_address}")
    try:
        data = client_socket.recv(1024).decode()
        if data:
            print(f"Received: {data} from {client_address}")
            client_socket.sendall("Message Received!".encode())
    except Exception as e:
        print(f"Error handling client {client_address}: {e}")
    finally:
        client_socket.close()
        print(f"Connection closed for {client_address}")

def start_server():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        server_socket.bind((HOST,PORT))
        server_socket.listen()
        print(f"server Listening on {HOST}: {PORT}.....")

        while True:
            try:
                client_socket, client_address = server_socket.accept()
                client_thread = threading.Thread(target=handle_client, args=(client_socket, client_address), daemon=True)
                client_thread.start()
            except Exception as e:
                print(f"[ERROR] Exception occurred: {e} ")
           



if __name__ == "__main__":
    start_server()