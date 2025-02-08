import asyncio
import websockets
from ollama import chat

connected_clients = set()

async def handler(websocket, path):
    """Handles incoming messages and connections."""
    connected_clients.add(websocket)
    try:
        async for message in websocket:
            print(f"Received: {message}")
            await send_message(websocket, message)
    except websockets.exceptions.ConnectionClosed:
        print("Client disconnected")
    finally:
        connected_clients.remove(websocket)

async def send_message(websocket, message: str):
    stream = chat(
        model='deepseek-r1:1.5b',
        messages=[{'role': 'user', 'content': f'{message} write point wise'}],
        stream=True,
    )

    for chunk in stream:
        text = chunk['message']['content']
        print(text)
        await websocket.send(text)

async def main():
    """Starts the WebSocket server."""
    server = await websockets.serve(handler, "localhost", 8765)
    print("WebSocket server started on ws://localhost:8765")
    await server.wait_closed()

if __name__ == "__main__":
    asyncio.run(main())
