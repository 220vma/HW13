from functools import partial


def suppressDecorator(func):
    def wrapper(x, y):
        try:
            func(x, y)
            print('Not Except')
        except:
            print('With Except')
    return wrapper


@suppressDecorator
def function(x, y):
    l = x/0
    i = y + 'hello'


function(2, 23)


def function(x, y):
    l = x / 0
    i = y + 'hello'


class Supress:
    def __enter__(self):
        print('Запуск менеджера контекста')

    def __exit__(self, type, value, traceback):
        print("Выполнено" + (" (с исключением)" if type else ""))
        return True


with Supress():
    function(3, 4)