import math


def main():
    square = int(input('Square: '))
    price = int(input('The price of 5 liter color: '))
    print('Number container color', get_container_for_paint(square))
    print('Time', get_time_work(square))
    print('Price color', get_price_color(square, price))
    print('Price work', )


def get_container_for_paint(square):
    value = square * 0.5 / 5
    return math.ceil(value)


def get_time_work(square):
    value = square * 0.8 / 8
    return value


def get_price_color(square, price):
    value = price * get_container_for_paint(square)
    return value

def get_price_work():


main()



