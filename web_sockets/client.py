 
import asyncio
import websockets

async def send_file():
    async with websockets.connect("ws://localhost:8765") as websocket:
        with open("/home/ewald/Desktop/PycharmProjects/server_client/stuff.txt", 'rb') as file:
            while True:
                chunk = file.read(1024)
                if not chunk:
                    break
                await websocket.send(chunk)
            await websocket.send("EOF")

asyncio.get_event_loop().run_until_complete(send_file())

