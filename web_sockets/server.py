
import asyncio
import websockets

async def receive_file(websocket, path):
    with open("received_file.txt", 'wb') as file:
        while True:
            data = await websocket.recv()
            if data == "EOF":
                break
            file.write(data)

start_server = websockets.serve(receive_file, "localhost", 8765)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
