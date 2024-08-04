import asyncio
import websockets
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import threading


def graph():
    file_path = "/home/ewald/Desktop/PycharmProjects/server_client/web_sockets/received_file.txt"
    integers_list = []

    with open(file_path, "r") as file:
        for line in file:
            integer = int(line.strip())
            integers_list.append(integer)

    print(integers_list)

    x = list(range(1, len(integers_list) + 1))
    y = integers_list

    plt.bar(x, y, label="BAR")
    plt.xlabel("Index")
    plt.ylabel("Value")
    plt.title("Graph Test")
    plt.legend()
    plt.show()
    asyncio.sleep(2)
    plt.close(all)


async def receive_file(websocket, path):
    with open("received_file.txt", 'wb') as file:
        while True:
            data = await websocket.recv()
            if data == "EOF":
                break
            file.write(data)
    threading.Thread(target=graph).start()

start_server = websockets.serve(receive_file, "localhost", 8765)

async def main():
    async with start_server:
        await asyncio.Future()

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()

