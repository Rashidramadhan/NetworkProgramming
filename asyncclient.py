import asyncio

HOST = '127.0.0.1'
PORT = 9090

async def start_client():
    """Asynchronous client connection."""
    reader, writer = await asyncio.open_connection(HOST, PORT)

    message = input("Enter message to send: ")
    writer.write(message.encode())
    await writer.drain()

    response = await reader.read(1024)
    print(f"Server response: {response.decode()}")

    writer.close()
    await writer.wait_closed()

if __name__ == "__main__":
    asyncio.run(start_client())
