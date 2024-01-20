#Nested functions

# def outer_func():
#     print("i am outer")
#
#     def inner_func_all():
#         print("I am inner1")
#
#
#     return inner_func_all
#
#
# func = outer_func()
# print(func)

import time

def delay_deco(function):
    def wrapper_func():
        print("\n")
        time.sleep(2)
        function()
    return wrapper_func


@delay_deco
def say_hello():
    print("Hello")

@delay_deco
def say_hi():
    print("Hi")


@delay_deco
def say_bye():
    print("Bye")



say_hello()
say_hi()
say_bye()
