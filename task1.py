# -*- coding: utf-8 -*-
# !/usr/bin/env python
# Базовые структуры данных
# Домашнее задание
# Описание домашнего задания и формат сдачи
# В домашнем задании необходимо решить предложенные задачи по программированию
# – вписать свой код в ячейки после условий задач вместо комментария
# ### YOUR CODE HERE ### в файле jun_anl_data_structures.ipynb и сохранить изменения
# NB! Во всех заданиях обязательно наличие выдачи.
# Индексация списка
test_list = [[[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]],
             [[21, 22, 23, 24, 25, 26, 27, 28, 29, 30], [31, 32, 33, 34, 35, 36, 37, 38, 39, 40]],
             [[41, 42, 43, 44, 45], [46, [47, 48], 49, 50], [51, 52, 53, 54, 55], [56, 57, 58, 59, 60]],
             [61, 62, 63, [64, 65, 66, 67, 68, 69, 70, 71], 72, 73, 74, [75, [76, 77, 78], 79], 80],
             [81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100]]

# 1. Из приведенного выше списка списков выведите с помощью индексов число 7.
print(test_list[0][0][6])

# 2. Из приведенного выше списка списков выведите с помощью индексов число 49.
print(test_list[2][1][2])

# 3. Из приведенного выше списка списков выведите с помощью индексов число 78.
print(test_list[3][7][2])

# 4. Из приведенного выше списка списков выведите с помощью индексов (используя отрицательные значения) число 99.
print(test_list[-1][-2])

# 5. Из приведенного выше списка списков сделайте срез с числом 74.
print(test_list[3][6:7])

# 6. Из приведенного выше списка списков сделайте срез с числами 47, 48.
print(test_list[2][1][1:2])

# 7. Из приведенного выше списка списков сделайте срез с числами 77, 78.
print(test_list[3][7][1][1:3])

# 8. С помощью функции range сгенерируйте следующую последовательность:
# [0, 1, 2, 3, 4]
sequence = list(range(5))
print(sequence)

# 9. С помощью функции range сгенерируйте следующую последовательность:[3, 4]
sequence = list(range(3, 5))
print(sequence)

# 10. С помощью функции range сгенерируйте следующую последовательность:[4, 8, 12, 16]
sequence = list(range(4, 20, 4))
print(sequence)

# 11. С помощью функции range сгенерируйте следующую последовательность:[16, 12, 8, 4]
sequence = list(range(16, 0, -4))
print(sequence)

# 12. С помощью функции range сгенерируйте следующую последовательность:[0, 5, 10]
sequence = list(range(0, 15, 5))
print(sequence)

# 13. С помощью функции range сгенерируйте следующую последовательность:[10, 5, 0]
sequence = list(range(10, -1, -5))
print(sequence)

# 14. С помощью функции range сгенерируйте следующую последовательность:[-10, -9, -8, -7, -6, -5, -4, -3, -2, -1]
sequence = list(range(-10, 0))
print(sequence)

# 15. С помощью функции range сгенерируйте следующую последовательность:[-10, -16, -22, -28, -34]
sequence = list(range(-10, -35, -6))
print(sequence)

# Операторы и типы данных
# Этот блок должен быть решен БЕЗ использования готовых функций и сторонних библиотек. Используйте операторы.
# 16. Часы показывают время в формате h:mm:ss (количество часов (от 0 до 23),
# двузначное количество минут, двузначное количество секунд). Количество минут
# и секунд при необходимости дополняются до двузначного числа нулями.
# Программа должна запрашивать количество секунд S, которое прошло с начала суток,
# и выводить в формате h:mm:ss, какое время будут показывать часы.
# Формат ввода:
# 3600
# Формат вывода:
# 1:00:00

time = int(input("Введите количество секунд: "))
hours = time // 3600
minutes = (time % 3600) // 60
seconds = time % 60
formatted_time = f"{hours}:{minutes:02d}:{seconds:02d}"
print(formatted_time)

# 17.
# Машина выезжает на нулевой километр МКАД и едет по часовой стрелке
# с постоянной скоростью V километров в час.
# На каком километре МКАД машина окажется через T часов?
# Длина МКАД: 109 км.
# Формат ввода:
# 60
# 1
# Формат вывода:
# 60

speed = int(input("Введите скорость машины (км/ч): "))
time = int(input("Введите время движения (ч): "))
m_kad_length = 109
position = (speed * time) % m_kad_length
print(position)

# 18.
# Напишите программу, которая запрашивает целое пятизначное число и выводит сумму его цифр.
# Формат ввода:
# 11111
# Формат вывода:
# 5

number = int(input("Введите целое пятизначное число: "))
my_str = str(number)
number = int(my_str[0]) + int(my_str[1]) + int(my_str[2]) + int(my_str[3]) + int(my_str[4])
print(type(number))

# 19. Напишите программу, которая запрашивает целое четырехзначное число
# и меняет местами его две первые и две последние цифры.
# Формат ввода:
# 5236
# Формат вывода:
# 3652

number = int(input("Введите целое четырехзначное число: "))
my_str = str(number)
number = int(my_str[3] + my_str[2] + my_str[0] + my_str[1])
print(type(number))

# 20. Напишите программу, которая на основании параметра D (сколько километров в день преодолевает машина),
# рассчитывает сколько дней она затратит на путь длиной P километров.
# Формат ввода:
# 105
# 120
# Формат вывода:
# 2

speed_per_day = int(input("Сколько километров в день преодолевает машина (D): "))
total_distance = int(input("Длина пути в километрах (P): "))
days_required = (total_distance + speed_per_day - 1) // speed_per_day
print(days_required)

# 21.
# Напишите программу, которая считает, сколько рублей и копеек нужно заплатить за N авокадо,
# если один авокадо стоит R рублей и K копеек.
# Формат ввода:
# 40 20
# 5
# Формат вывода:
# 201 руб. 00 коп.

price_rub = int(input("Введите цену в рублях: "))
price_kop = int(input("Введите цену в копейках: "))
quantity = int(input("Введите количество авокадо (N): "))
total_cents = (price_rub * 100 + price_kop) * quantity
total_rub = total_cents // 100
total_kop = total_cents % 100
print(f"{total_rub} руб. {total_kop:02d} коп.")

# 22. Пусть организаторы мероприятия неправильно составили гугл-форму
# и просили людей указывать ФИО в неправильном порядке.
# Сначала спрашивали имя, потом отчество, затем фамилию.
# Напишите программу, которая будет переставлять ФИО в нужный порядок.
# Формат ввода:
# Иван Иванович Иванов
# Формат вывода:
# Иванов Иван Иванович

my_data = str(input("Укажите своё Имя, Отчество, Фамилию через пробел: "))
my_list = my_data.split(" ")
my_text = str(my_list[2] + " " + my_list[0] + " " + my_list[1])
print(my_text)

# 23. У вас есть список с заказом в ресторане.
# Напишите программу, которая меняет указанное по названию блюдо на другое.
# При этом новое блюдо в списке будет расположено на месте того, что было заменено.
# Формат ввода:
# белое вино
# красное вино
# Формат вывода:
# ['красное вино', 'салат Цезарь', 'паста Карбонара', 'чизкейк', 'шоколадный сорбет']

order = ['белое вино', 'салат Цезарь', 'паста Карбонара', 'чизкейк', 'шоколадный сорбет']
old_dish = str(input("Введите стaрое блюдо: "))
new_dish = str(input("Введите новое блюдо: "))
i = order.index(old_dish)
order[i] = new_dish
print(order)

# Вам дан словарь с расписанием на неделю.
diary = {'понедельник': {
    'утро': ['погулять с собакой'],
    'день': [],
    'вечер': ['погулять с собакой']
},
    'вторник': {
        'утро': ['погулять с собакой'],
        'день': [],
        'вечер': ['погулять с собакой']
    },
    'среда': {
        'утро': ['погулять с собакой'],
        'день': [],
        'вечер': ['погулять с собакой']
    },
    'четверг': {
        'утро': ['погулять с собакой'],
        'день': [],
        'вечер': ['погулять с собакой']
    },
    'пятница': {
        'утро': ['заехать в шиномонтаж', 'помыть машину'],
        'день': [],
        'вечер': ['поход в театр', 'ужин в кафе']
    },
    'суббота': {
        'утро': [],
        'день': [],
        'вечер': []
    },
    'воскресенье': {
        'утро': [],
        'день': [],
        'вечер': []
    }}
# 24. Удалите ключи суббота и воскресенье.
# Вместо них добавьте пару, где ключ это кортеж суббота, воскресенье,
# а значение – список с делом посадить цветы на даче. Можно ли сделать ключ суббота, воскресенье списком?

diary.pop('суббота')
diary.pop('воскресенье')
diary[('суббота', 'воскресенье')] = {'посадить цветы на даче'}
print(diary)

# 25. Добавьте в список дел во вторник утром поход к зубному.

diary['вторник']['утро'][0] = 'поход к зубному'
print(diary)

# 26. Замените поход в театр на поход в кино в списке дел в пятницу вечером.

diary['пятница']['вечер'][0] = 'поход в кино'
print(diary)

# 27. Ваш друг вернется из отпуска на один день раньше, поэтому он заберет свою собаку в среду, а не в четверг.
# Удалите дело погулять с собакой из соответствующих списков.

del diary['среда']['утро'][0]
del diary['среда']['вечер'][0]
del diary['четверг']['утро'][0]
del diary['четверг']['вечер'][0]
print(diary)

# 28. Выведите второе дело из списка дел, которые вам нужно сделать в пятницу утром.

print(diary['пятница']['утро'][1])
