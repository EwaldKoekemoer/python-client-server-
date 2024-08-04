import asyncio
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import threading
import websockets


def sort_data_graph():
    file_path = "/home/ewald/Desktop/PycharmProjects/server_client/web_sockets/received_file.txt"
    integers_list = []

    # Read and process the file
    with open(file_path, "r") as file:
        for line in file:
            integer = int(line.strip())
            integers_list.append(integer)

    # Sort data
    sorted_data = sorted(integers_list)

    # Create a new figure for the sorted data
    fig1, ax1 = plt.subplots()
    ax1.bar(range(1, len(sorted_data) + 1), sorted_data, label="Sorted Data")
    ax1.set_xlabel("Index")
    ax1.set_ylabel("Value")
    ax1.set_title("Sorted Data Graph")
    ax1.legend()
    plt.show()

def graph():
    file_path = "/home/ewald/Desktop/PycharmProjects/server_client/web_sockets/received_file.txt"
    integers_list = []

    # Read and process the file
    with open(file_path, "r") as file:
        for line in file:
            integer = int(line.strip())
            integers_list.append(integer)

    # Create a new figure for the unsorted data
    fig2, ax2 = plt.subplots()
    ax2.bar(range(1, len(integers_list) + 1), integers_list, label="Data")
    ax2.set_xlabel("Index")
    ax2.set_ylabel("Value")
    ax2.set_title("Data Graph")
    ax2.legend()
    plt.show()

async def receive_file(websocket, path):
    with open("received_file.txt", 'wb') as file:
        while True:
            data = await websocket.recv()
            if data == "EOF":
                break
            file.write(data)
    threading.Thread(target=graph()).start()
    threading.Thread(target=sort_data_graph()).start()

plt.close('all')

start_server = websockets.serve(receive_file, "localhost", 8765)

async def main():
    async with start_server:
        await asyncio.Future()

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
