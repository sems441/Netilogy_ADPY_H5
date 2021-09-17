import datetime
import random


def parametrized_decor(file_name):
    def second_function(function):
        def new_function(*args, **kwargs):
            name_func = second_function.__name__
            time = datetime.datetime.now()
            result = function(*args, **kwargs)
            attribute = function.__name__
            with open(f"{file_name}.txt", "w", encoding="utf-8") as file_write:
                file_write.write(f"{time} Имя функции: {name_func} Имя атрибута: {attribute} "
                                 f"Результат первой функции: {result}\n")
            return result
        return new_function
    return second_function


name = input("Введите имя файла ")


@parametrized_decor(file_name=name)
def first_function():
    print("запущена first_function")
    return random.randint(0, 10)


first_function()
