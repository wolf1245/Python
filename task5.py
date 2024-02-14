#!/usr/bin/env python
# coding: utf-8

# # Исключения
# ## Домашняя работа
# ### Вопросы по лекциям.

# Как поймать вообще все ошибки, которые могут произойти?

# **Ответ:**
# с помощью вcтроенного try and except

# Сколько раз подряд можно указывать except?

# **Ответ:**
# множество

# Вы хотите с помощью print вывести название ошибки в консоль, как это сделать?

# **Ответ:**
# except ZeroDivisionError as exc:
# print(f'вот что пошло не так {type(exc)}')

# Вы хотите с помощью print вывести параметры ошибки в консоль, как это сделать?

# **Ответ:**
# except ZeroDivisionError as exc:
# print(f'вот что пошло не так параметры {exc.args}')

# Что такое DeprecationWarning?

# **Ответ:**
# Предупреждения об устаревании — это способ оповещения разработчиков Python о том,
# что некоторые части кода скоро могут стать нерабочими

# ### Разминочные задания.
# Вам даны две функции. По исследуйте, какие ошибки могут возникнуть при их реализации. Обработайте эти ошибки.

def div():
    for i in range(2):
        try:
            x = int(input("enter a number: "))
            y = int(input("enter another number: "))
            print(x, '/', y, '=', x / y)
        except ZeroDivisionError as exc:
            print(f"внутри div() что-то пошло не так: {exc} - параметры ошибки {exc.args}")
        else:
            print("Все по плану")


div()


def sumOfPairs(L1, L2):
    try:
        sum = 0
        sumOfPairs = []
        for i in range(len(L1)):
            sumOfPairs.append(L1[i] + L2[i])

        print("sumOfPairs = ", sumOfPairs)
    except TypeError as exc:
        print(f" внутри sumOfPairs() что-то пошло не так {type(exc)} c параметром {exc.args}")


sumOfPairs(5, 7)


# ### Задание 1.
# 
# Есть файл с протоколом регистраций пользователей на сайте (registrations.txt).
# Каждая строка содержит информацию об имени, электронной почте и возрасте человека.
# 
# 
# Надо проверить данные из файла, для каждой строки:
#  - присутствуют все три поля
#  - поле имени содержит только буквы
#  - поле email содержит @ и точку(.)
#  - поле возраст является числом от 10 до 99
# 
# В результате проверки нужно сформировать два файла
#  - registrations_good.log для правильных данных, записывать строки как есть
# - registrations_bad.log для ошибочных, записывать строку и вид ошибки.
# 
# Для валидации строки данных написать метод, который может выкидывать исключения:
#  - НЕ присутствуют все три поля: ValueError
#  - поле имени содержит НЕ только буквы: NotNameError (кастомные исключение)
#  - поле email НЕ содержит @ и (точку): NotEmailError (кастомные исключение)
#  - поле возраст НЕ является числом от 10 до 99: ValueError
# Вызов метода обернуть в try-except.


class NotNameError(Exception):
    pass


class NotEmailError(Exception):
    pass


def validate_registration_line(line):
    """
    Метод для валидации строки данных регистрации пользователя.
    """
    # Разделяем строку на поля
    fields = line.strip().split()

    # Проверяем наличие всех трех полей
    if len(fields) != 3:
        raise ValueError("Не присутствуют все три поля")

    # Проверяем поле имени на наличие только букв
    if not fields[0].isalpha():
        raise NotNameError("Поле имени содержит НЕ только буквы")

    # Проверяем поле email на наличие @ и точки
    if '@' not in fields[1] or '.' not in fields[1]:
        raise NotEmailError("Поле email НЕ содержит @ и (точку)")

    # Проверяем поле возраст на то, что является числом от 1 до 99
    if not fields[2].isdigit() or not 1 <= int(fields[2]) <= 99:
        raise ValueError("Поле возраст НЕ является числом от 1 до 99")


# Открываем файл для чтения
with open("task5.txt", "r") as file:
    # Открываем файлы для записи правильных и ошибочных данных
    with open("registrations_good.log", "w") as good_file, open("registrations_bad.log", "w") as bad_file:
        # Проверяем каждую строку из файла
        for line in file:
            try:
                # Валидируем строку
                validate_registration_line(line)
                # Если успешно, записываем в файл с правильными данными
                good_file.write(line)
            except (ValueError, NotNameError, NotEmailError) as e:
                # Если возникла ошибка, записываем в файл с ошибками
                bad_file.write(f"{line.strip()} - {str(e)}\n")
