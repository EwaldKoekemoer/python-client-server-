import asyncio
import websockets
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import threading


def sort_data_graph():
    file_path = "/home/ewald/Desktop/PycharmProjects/server_client/web_sockets/received_file.txt"
    integers_list = []

    with open(file_path, "r") as file:
        for line in file:
            integer = int(line.strip())
            integers_list.append(integer)

    numbers = integers_list
    sorted_data = numbers.sort()

    print(integers_list)

    x = list(range(1, len(sorted_data) + 1))
    y = sorted_data

    plt.bar(x, y, label="BAR")
    plt.xlabel("Index")
    plt.ylabel("Value")
    plt.title("sorted_data_graph")
    plt.legend()
    plt.show()
    asyncio.sleep(5)
    plt.close(all)

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
    plt.title("data_graph")
    plt.legend()
    plt.show()
    asyncio.sleep(5)
    plt.close(all)

async def receive_file(websocket, path):
    with open("received_file.txt", 'wb') as file:
        while True:
            data = await websocket.recv()
            if data == "EOF":
                break
            file.write(data)
    threading.Thread(target=graph()).start()
    #threading.Thread(target=sort_data_graph()).start()

start_server = websockets.serve(receive_file, "localhost", 8765)

async def main():
    async with start_server:
        await asyncio.Future()

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()

