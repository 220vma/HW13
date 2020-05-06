from contextlib import contextmanager
from time import time
from string import ascii_letters
from itertools import product

@contextmanager
def timer():
    try:
        start = time()
        yield ""
    finally:
        result = time() - start
        print("time: {:.2f}".format(result))

def listgen(count):
    p = product(ascii_letters, repeat=count)
    l = []
    for i in p:
        l.append(i)
    print("Выполнено")

if __name__ == "__main__":
    with timer() as t:
        listgen(10000)