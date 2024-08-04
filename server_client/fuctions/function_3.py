import asyncio
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
