# -*- coding: utf-8 -*-
# author: itimor

import datetime
import time

def timeout(func):
    def wrapper(*args, **kwargs):
        s_time = datetime.datetime.now()
        print (f'func decorator runing at {s_time}')
        func(*args, **kwargs)
        e_time = datetime.datetime.now()
        print (f'func decorator ending at {e_time}')
        const_time = (e_time - s_time).seconds
        print(f'func ececute const time {const_time} seconds.')
    return wrapper

# 类装饰器
class Timeout(object):
    def __init__(self, func):
        self._func = func

    def __call__(self, *args, **kwargs):
        s_time = datetime.datetime.now()
        print (f'class decorator runing at {s_time}')
        self._func(*args, **kwargs)
        e_time = datetime.datetime.now()
        print (f'class decorator ending at {e_time}')

@timeout
@Timeout
def foo(n):
    for i in range(n):
        time.sleep(1)
        print(i)

if __name__ == '__main__':
    foo(5)