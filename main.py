import datetime
import random


def first_function():
    print("запущена first_function")
    return random.randint(0, 10)


def second_function(function, file_name):

    def new_function():
        result = function()
        with open(f"{file_name}.txt", "w", encoding="utf-8") as file_write:
            time = datetime.datetime.now()
            name_func = second_function.__name__
            attribute = function.__name__
            file_write.write(f"{time} Имя функции: {name_func} Имя атрибута: {attribute} "
                             f"Результат первой функции: {result}\n")
        return result
    return new_function


name = input("name: ")
first_function = second_function(first_function, name)
first_function()
