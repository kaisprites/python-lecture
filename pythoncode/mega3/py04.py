def plus(x, y):
    return x+y


def minus(x, y):
    return x-y


def mult(x, y):
    return x*y


def div(x, y):
    return x/y


class Dog:
    name = '멈무'

    def __init__(self):
        print('강아지 생성자')

    def __str__(self):
        return self.name

    def bark(self):
        print('멍멍')