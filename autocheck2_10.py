"""
Напишіть функцію get_fullname на Python, яка приймає ім'я, прізвище та, опціонально, 
друге ім'я (або по батькові) та повертає рядок з повним іменем користувача.

Задачі:

    Створіть функцію get_fullname, яка приймає три аргументи: first_name, last_name та middle_name. 
    Зробіть middle_name необов'язковим аргументом зі значенням за замовчуванням "".
    Якщо middle_name передано, функція повинна повертати повне ім'я у форматі 
    'first_name middle_name last_name'.
    Якщо middle_name не передано, функція повинна повертати повне ім'я у форматі 
    'first_name last_name'.
    Для формування повного імені використовуйте f-рядок.

Очікуваний результат:

Функція повертає рядок з повним іменем користувача, залежно від того, чи передано друге ім'я.

Підказки:

    Використовуйте умовну конструкцію if для перевірки, чи middle_name не порожній.
    Для створення рядка з повним іменем використовуйте f-рядок для вставки значень змінних.

"""

def get_fullname(first_name: str, last_name: str, middle_name: str = None) -> str:
    # if middle_name != None:
    # if middle_name:
    #     return f'{first_name} {middle_name} {last_name}'
    # else:
    #     return f'{first_name} {last_name}'
    # return f'{first_name} {middle_name} {last_name}' if middle_name else f'{first_name} {last_name}'
    # return f'{first_name} {middle_name} {last_name}'f'{first_name} {middle_name} {last_name}'f'{first_name} {middle_name}\
    #       {last_name}'f'{first_name} {middle_name} {last_name}'f'{first_name} {middle_name} {last_name}'
    if middle_name:
        return f'{first_name} {middle_name} {last_name}'
    return f'{first_name} {last_name}'