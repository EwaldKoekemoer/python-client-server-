import random as rnd

def generate_data():
    this = True
    while this:
        numbers = (1, 5, 10, 13, 20, 8, 17, 3)
        amount = 0
        maxi = 20
        with open("/home/ewald/Desktop/PycharmProjects/server_client/stuff.txt", 'w') as file:
            while amount < maxi:
                amount += 1
                random_data = rnd.choice(numbers)
                file.write(f"{random_data}\n")
        this = False

generate_data()
