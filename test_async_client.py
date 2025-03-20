import asyncio
import time

HOST = "127.0.0.1"
PORT = 9090
NUM_CLIENTS = 500  # Number of concurrent clients

async def client_task(client_id):
    """Each async client connects to the server, sends a message, and receives a response."""
    try:
        reader, writer = await asyncio.open_connection(HOST, PORT)
        message = f"Hello from async client {client_id}"
        writer.write(message.encode())
        await writer.drain()  # Ensure data is sent

        response = await reader.read(1024)
        print(f"[Client {client_id}] Server response: {response.decode()}")

        writer.close()
        await writer.wait_closed()
    except Exception as e:
        print(f"[Client {client_id}] Error: {e}")

async def main():
    """Launch multiple async clients simultaneously."""
    start_time = time.time()
    tasks = [client_task(i) for i in range(NUM_CLIENTS)]
    await asyncio.gather(*tasks)
    elapsed_time = time.time() - start_time
    print(f"\n[INFO] {NUM_CLIENTS} async clients completed in {elapsed_time:.2f} seconds")

# Run the test
asyncio.run(main())
