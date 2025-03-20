import socket
import threading
import time

HOST = "127.0.0.1"
PORT = 9090
NUM_CLIENTS = 500  # Number of simultaneous clients

def client_task(client_id):
    """Each client connects to the server, sends a message, and receives a response."""
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
            client_socket.connect((HOST, PORT))
            message = f"Hello from client {client_id}"
            client_socket.sendall(message.encode())

            response = client_socket.recv(1024).decode()
            print(f"[Client {client_id}] Server response: {response}")

    except Exception as e:
        print(f"[Client {client_id}] Error: {e}")

# Start multiple clients simultaneously
start_time = time.time()
threads = []
for i in range(NUM_CLIENTS):
    thread = threading.Thread(target=client_task, args=(i,))
    threads.append(thread)
    thread.start()

# Wait for all clients to finish
for thread in threads:
    thread.join()

elapsed_time = time.time() - start_time
print(f"\n[INFO] {NUM_CLIENTS} clients completed in {elapsed_time:.2f} seconds")
