import asyncio
import websockets
import random as rnd

def generate_data():
    this = True
    while this:
        numbers1 = (1, 5, 10, 13, 20, 8, 17, 3, 24)
        numbers2 = (4, 7, 9, 12, 21, 15, 14, 2, 25)
        numbers3 = (6, 11, 13, 16, 18, 19, 22, 23)
        lists = (numbers1, numbers2, numbers3)
        amount = 0
        maxi = 20
        with open("/home/ewald/Desktop/PycharmProjects/server_client/stuff.txt", 'w') as file:
            while amount < maxi:
                amount += 1
                random_lists = rnd.choice(lists)
                random_data = rnd.choice(random_lists)
                file.write(f"{random_data}\n")
        this = False

async def send_file():
    async with websockets.connect("ws://localhost:8765") as websocket:
        with open("/home/ewald/Desktop/PycharmProjects/server_client/stuff.txt", 'rb') as file:
            while True:
                chunk = file.read(1024)
                if not chunk:
                    break
                await websocket.send(chunk)
            await websocket.send("EOF")

generate_data()
asyncio.get_event_loop().run_until_complete(send_file())
