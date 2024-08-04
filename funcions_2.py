import random as rnd

def generate_data():
    this = True
    while this:
        numbers = (1, 5, 10, 13, 20, 8, 17, 3)
        amount = 0
        maxi = 20
        while amount < maxi:
            amount += 1
            random_data = rnd.choice(numbers)
            print(random_data)
        this = False

generate_data()
