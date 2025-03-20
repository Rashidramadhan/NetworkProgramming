import asyncio

HOST = '127.0.0.1'
PORT = 9090

async def handle_client(reader, writer):
    """Handles a client asynchronously."""
    addr = writer.get_extra_info('peername')
    print(f"New connection from {addr}")

    try:
        data = await reader.read(1024)
        if data:
            message = data.decode()
            print(f"Received from {addr}: {message}")
            writer.write("Message Received!".encode())
            await writer.drain()  # Ensure data is sent
    except Exception as e:
        print(f"Error handling {addr}: {e}")

    print(f"Closing connection with {addr}")
    writer.close()
    await writer.wait_closed()

async def start_server():
    """Starts the asynchronous server."""
    server = await asyncio.start_server(handle_client, HOST, PORT)
    addr = server.sockets[0].getsockname()
    print(f"Server listening on {addr}")

    async with server:
        await server.serve_forever()

if __name__ == "__main__":
    asyncio.run(start_server())
