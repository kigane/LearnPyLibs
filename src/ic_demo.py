from datetime import datetime
import time
import numpy as np
import matplotlib.pyplot as plt
from icecream import install
install()


def time_format():
    return f'{datetime.now().strftime("%y-%m-%d %H:%m:%S")} | '

def plus_five(num):
    return num + 5

def hello(user:bool):
    if user:
        # print("I'm user")
        ic()
    else:
        # print("I'm not user")
        ic()
    return "hello"

if __name__ == '__main__':
    ic.configureOutput(prefix=time_format, includeContext=True)
    num1 = 30
    num2 = 40 
    ic("hello world!")

    ic(num1)
    ic(num2)
    ic(plus_five(4))
    hello(True)