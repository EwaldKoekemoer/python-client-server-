import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import asyncio

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
    asyncio.sleep(5)
    plt.close(all)

