import datetime
import random
# def printing_message():
#     print(f"Запущена функция printing_message")
#
# def new_func(func):
#     func()
#
# printing_message()
# x = printing_message
# my_list = []
# my_list.append(x)
# print("запуск через список")
# my_list[0]()
#
# print("запуск через функцию")
# new_func(printing_message)

def first_function():
    print("запущена first_function")
    return random.randint(0, 10)


def second_function(function, i_name):

    def new_function():
        print("код до result")
        result = function()
        with open(f"{i_name}.txt", "w", encoding="utf-8") as file_write:
            time = datetime.datetime.now()
            name = second_function.__name__
            atributs = function.__name__
            file_write.write(f"{time} {name} {atributs} {result}")

        print("код после result")
        return result
    return new_function

name = input("name: ")
first_function = second_function(first_function, name)
first_function()
