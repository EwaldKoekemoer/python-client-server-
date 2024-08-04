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

generate_data()
