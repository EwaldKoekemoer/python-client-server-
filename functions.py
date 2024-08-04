import random as rnd


def generate_data():
    this  = True
    while this:

        list = (1, 5, 10, 13, 20, 8, 17, 3)
        amount = 0
        maxi = 20
        while amount < maxi:
            amount += 1
            random_data = rnd.choice(list)
            print(random_data)

        this = False

data = generate_data()
print (data)